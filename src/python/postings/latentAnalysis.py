import collections
import gensim
import glob
import io
import itertools
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import pyLDAvis.gensim
import re
import os
import seaborn as sns
import tensorflow as tf
import warnings

from datetime import datetime
from gensim import corpora, models
from gensim.utils import simple_preprocess
from multiprocessing import Pool, cpu_count
from nltk import pos_tag, RegexpParser
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Embedding, Activation, Flatten
from tensorflow.keras.utils import to_categorical
from wordcloud import WordCloud

# Start the timer.
startTime = datetime.now()

# Ignore deprecation warnings.
warnings.simplefilter("ignore", DeprecationWarning)

# Seaborn color style for bar graphs.
sns.set_style("whitegrid")

# Stopwords used to remove unnecessary words from text.
en_stop = nltk.download("stopwords")
stopwords = set(stopwords.words("english"))

"""
Perform latent semantic analysis (LSA) and latent Dirichlet analysis (LDA)
on the job information. It uses the raw job description files as input,
creates a .csv of the LDA model, and then creates plots of the semantic content.
We perform latent analysis on both the raw input job files (in data/postings/raw/).

Usage: "python latentanalysis.py"

LDA assumes documents are produced from a mixture of topics. Those topics then generate words based on their
probability distribution, like the ones in our walkthrough model. In other words, LDA assumes a document is
made from the following steps:
1. Determine the number of words in a document. Let's say our document has 6 words.
2. Determine the mixture of topics in that document. For example, the document might contain 1/2 the topic "health" and
    1/2 the topic "vegetables."
3. Using each topic's multinomial distribution, output words to fill the document's word slots. In our example, the "health"
    topic is 1/2 our document, or 3 words. The "health" topic might have the word "diet" at 20% probability or "exercise"
    at 15%, so it will fill the document word slots based on those probabilities. Given this assumption of how documents are
    created, LDA backtracks and tries to figure out what topics would create those documents in the first place.
"""

class ReadFiles(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname), encoding="utf-8"):
                yield simple_preprocess(line.lower())

def add_new_word(newword, newvector, newindex, embeddingmatrix, word2id):
    """
    Add a new word to the existing matrix of word embeddings.
    """
    # Insert the vector before the given idnex along axis 0.
    embeddingmatrix = np.insert(embeddingmatrix, [newindex], [newvector], axis=0)
    # Update the indices of words that follow the new word.
    word2id = {word: (index + 1) if index >= newindex else index for word, index in word2id.items()}
    word2id[newword] = newindex
    return embeddingmatrix, word2id

def define_context_sensitive_model(embeddingmatrix, class_count):
    """
    Create and return a part-of-speech (POS) model that takes tagged word and context
    as input.
    """
    vocablen = len(embeddingmatrix)
    total_span = 5
    model = Sequential() # This model is a stack of layers we add one by one.
    model.add(Embedding(input_dim=vocablen, output_dim=300, weights=[embeddingmatrix], input_length=total_span))
    model.add(Flatten())
    model.add(Dense(50)) # 50 is the hidden size for the dense layer
    model.add(Activation("tanh")) # tanh activation function as a sigmoid approximation
    model.add(Dense(class_count))
    model.add(Activation("softmax")) # for normalizing the input vector to probabilit distribution
    model.compile(optimizer=tf.train.AdamOptimizer(), loss="categorical_crossentropy", metrics=["accuracy"])
    return model

def evaluate_model(model, id2word, xtest, ytest):
    """
    Evaluate model by computing the accuracy of predictions and print out the most
    mistagged words.
    """
    # Get accuracy.
    _, acc = model.evaluate(xtest, ytest)
    print("Accuracy: %.2f" % acc)
    # Get most commonly mistagged words.
    ypred = model.predict_classes(xtest)
    errorcounter = collections.Counter()
    for i in range(len(xtest)):
        correcttagid = np.argmax(ytest[i])
        if ypred[i] != correcttagid:
            if isinstance(xtest[i], np.ndarray):
                word = id2word[xtest[i][2]]
            else:
                 word = id2word[xtest[i]]
            errorcounter[word] += 1
    with open("output/latent/errors", "w") as file:
        print("Most common errors:\n", errorcounter.most_common(10))
        file.write("Most common errors:\n")
        for i in errorcounter.most_common(10):
            file.write(str(i))

def get_int_data(twords, word2id, tag2id):
    """
    Replace words and tags with correspondings id's and separate words
    (features) from the tags (labels).
    """
    X, Y = [], [] # X for word id's and Y for tag id's
    count = 0 # count of unknown words (words for which we don't have a representation)
    for word, tag in twords:
        Y.append(tag2id.get(tag))
        if word in word2id: # If we have the info in the dictionary
            X.append(word2id.get(word))
        else:
            X.append(0) # 0 is unknown index
            count += 1 # No representation
    print("Percentage of unknown words: %.3f" % (count/len(twords)))
    return np.array(X), np.array(Y)

def get_tag_vocab(twords):
    """
    For input tagged words twords in the tuple form (word, position), return a
    dictionary mapping POS-tags (parts of speech tags) to unique ids.
    """
    tag2id = {}
    for i, j in twords:
        tag2id.setdefault(j, len(tag2id))
    return tag2id

def get_window_int_data(twords, word2id, tag2id):
    """
    Replace all words and tags with their corresponding id's and generate an array
    of labels id's Y and the training data X, which consists of arrays of word indices.
    """
    X, Y = [], []
    count = 0 # unknown count
    span = 5 # span of sliding window
    buffer = collections.deque(maxlen=span)
    padding = [[("EOS", None)] * 2]
    buffer += padding + twords[:2]
    for i in (twords[2:] + padding):
        buffer.append(i)
        windowids = np.array([word2id.get(word) if (word in word2id) else 0 for (word, _) in buffer])
        X.append(windowids)
        middleword, middletag = buffer[2]
        Y.append(tag2id.get(middletag))
        if middleword not in word2id:
            count += 1
    print("Percentage of unknown words: %.3f" % (count/len(twords)))
    return np.array(X), np.array(Y)

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while os.getcwd().split("/")[-1] != "journalism":
    os.chdir("..")

# Check if the output file directory exists. If not, make it.
if not os.path.isdir("output/latent"):
    os.mkdir("output/latent")

# Create the list of tokens from all the files in the directory.
tokenizedlist = ReadFiles("data/postings/raw")
print("Files parsed.")

# Remove empty lists.
tokenizedlist = [x for x in tokenizedlist if x != []]

# Create the gensim dictionary.
mydict = corpora.Dictionary(tokenizedlist)
print("Dictionary created.")

# Save the gensim dictionary.
mydict.save("output/latent/mydict.dict")

# Create the gensim corpus.
bowcorpus = [mydict.doc2bow(token) for token in tokenizedlist]
print("Corpus created.")

# Save the gensim corpus.
corpora.MmCorpus.serialize("output/latent/corpus.mm", bowcorpus)

# Create and fit the LDA model using our corpus and dictionary with gensim.
lda = models.LdaMulticore(corpus=bowcorpus,
                         id2word=mydict,
                         random_state=100,
                         num_topics=7,
                         passes=10,
                         chunksize=1000,
                         batch=False,
                         alpha="asymmetric",
                         decay=0.5,
                         offset=64,
                         eta=None,
                         eval_every=0,
                         iterations=100,
                         gamma_threshold=0.001,
                         per_word_topics=True)

print("LDA model created.")
lda.save("output/latent/topic.model")

# Create wordlcoud.
wc = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color="steelblue")
wordstring = ""
for item in mydict.token2id:
    tempstring = str(item) * mydict.token2id[item]
    wordstring += tempstring
wcimg = wc.generate_from_text(wordstring)
wcimg.to_file("output/latent/wordcloud.png")
print("Wordcloud created.")

# Visualize the topics.
data = pyLDAvis.gensim.prepare(lda, bowcorpus, mydict)
pyLDAvis.save_html(data, "output/latent/ldavis_prepared.html")
print("Topics visualized.")

"""
Now we will learn how to train our own embeddings using the gensim library, how to process text data to feed into a neural model,
how to use pre-trained word embeddings in Keras models, and how to build simple context-dependent and context-independent word classification models.
This neural network can be further improved with more training and test data.
"""

# Building embedding.
w2v = models.Word2Vec(tokenizedlist, size=300, window=5, min_count=5, negative=15, iter=10, workers=cpu_count())
wvec = w2v.wv
embeddingmatrix = wvec.vectors
print("Embedding built.")

# Create the parts of speech (PODS) taglist used for determining how
# words relate to one another.
taglist = [pos_tag(token) for token in tokenizedlist]
print("Tags extracted.")

# Remove empty lists.
taglist = [x for x in taglist if x != []]

# Build training and test sets.
splitindex = int(len(taglist)*.8) # The index at which we split between training and test data
trainwords, testwords = [], [] # Initialize arrays for training and test word data.
for i in range(len(taglist)):
    pair = taglist[i]
    if i < splitindex:
        trainwords.append(pair)
    else:
        testwords.append(pair)

# Build word-to-id mapping dictionary.
word2id = {k: v.index for k, v in wvec.vocab.items()}

# Create id-to-word mapping dictionary.
id2word = sorted(word2id, key=word2id.get)

# Build tag-to-id mapping dictionary.
tag2id = get_tag_vocab(trainwords)
print("Mappings created.")

# Get the features separate from tags.
Xtrain, Ytrain = get_int_data(trainwords, word2id, tag2id)
Xtest, Ytest = get_int_data(testwords, word2id, tag2id)
print("Features extracted.")

# One-hot encode the tag indices.
Ytrain, Ytest = to_categorical(Ytrain), to_categorical(Ytest)

# Keep track of unknown embeddings.
unkvec = embeddingmatrix.mean(0)
embeddingmatrix, word2id = add_new_word("NaN", unkvec, 0, embeddingmatrix, word2id)

# Create model.
pos_model = define_context_sensitive_model(embeddingmatrix, len(tag2id))
print("Model created.")

# Train.
pos_model.fit(Xtrain, Ytrain, batch_size=128, epochs=1, verbose=1)
pos_model.summary()
print("Model trained.")

# Evaluate.
evaluate_model(pos_model, id2word, Xtest, Ytest)
print("Model evaluated.")

# Build context-dependent model by creating a random end-of-sequence vector.
eos_vector = np.random.standard_normal(300)
embeddingmatrix, word2id = add_new_word("EOS", eos_vector, 1, embeddingmatrix, word2id)
with open("output/latent/matrix", "w") as file:
    for line in embeddingmatrix:
        file.write(str(line))

# Print how long this script took to run.
print("Total run time : " + str(datetime.now() - startTime))
