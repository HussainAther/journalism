import matplotlib.pyplot as plt
import numpy as np

from gensim import corpora, models
from gensim.utils import simple_preprocess

my_docs = ["Who let the dogs out?",
           "Who? Who? Who? Who?"]

tokenized_list = [simple_preprocess(doc) for doc in my_docs]

mydict = corpora.Dictionary()
bowcorpus = [mydict.doc2bow(doc, allow_update=True) for doc in tokenized_list]

"""
Create and save the TF-IDF (tfidf) model. In information retrieval, tf–idf or TFIDF, short for term frequency–inverse document frequency, is a
numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.[1] It is often used as a weighting
factor in searches of information retrieval, text mining, and user modeling. The tf–idf value increases proportionally to the number of times a word
appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words
appear more frequently in general. tf–idf is one of the most popular term-weighting schemes today; 83% of text-based recommender systems in digital libraries use tf–idf.
"""

tfidf = models.TfidfModel(bowcorpus, smartirs="ntc")
tfidf.save("output/latent/topic.tfidfmodel")
print("TF IDF model created.")

# Word TF-IDF dictionary.
toptfidf = {}
# Show weights.
for i in tfidf[bowcorpus]:
    for j in [[mydict[id], np.around(freq, decimals=2)] for id, freq in i]:
        toptfidf[j[0]] = j[1] # Save the word TF-IDf score.

# Sort the tfidf dictionary by values and retrieve the top 10 topics by TF-IDF.
s = [(k, toptfidf[k]) for k in sorted(toptfidf, key=toptfidf.get, reverse=True)][:10]
topwords, topscores = [], []
for k, v in s:
    topwords.append(k)
    topscores.append(v)
xpos = np.arange(len(topscores))

# Plot the highest tfidf scores.
plt.figure(2, figsize=(15, 15))
plt.subplot(title="10 highest TF-IDF scores")
sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
sns.barplot(xpos, topscores, palette="husl")
plt.xticks(xpos, topwords, rotation=90)
plt.xlabel("Words")
plt.ylabel("TF-IDF score")
plt.savefig("output/latent/10tfidf.png")

# Retrieve the top 10 most frequent words and their corresponding frequencies.
s = sorted(np.array([[(mydict[id], freq) for id, freq in cp] for cp in bowcorpus]))[:10]
topwords, topscores = [], []
for i in s:
    for k, v in i:
        topwords.append(k)
        topscores.append(v)
xpos = np.arange(len(topscores))

# Plot the most common words.
plt.figure(2, figsize=(15, 15))
plt.subplot(title="10 most common words")
sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
sns.barplot(xpos, topscores, palette="husl")
plt.xticks(xpos, topwords, rotation=90)
plt.xlabel("Words")
plt.ylabel("TF-IDF score")
plt.savefig("output/latent/10mostcommon.png")
print("Frequency plots created.")
