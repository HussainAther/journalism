import json
import keras
import keras.preprocessing.text as kpt
import nltk
import numpy as np
import os
import pandas as pd
import psycopg2
import re
import seaborn as sns
import sklearn
import tqdm

from keras.layers import Acivation, Dense, Dropout
from keras.models import modle_from_json, Sequential
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from postgres_credentials import *
from pycorenlp import StanfordCoreMLP
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sqlalchemy import create_engine
from wordcloud import WordCloud

"""
Visualizing Twitter followers to analyze the public opinion of "anime".
"""

def base(tabletweets):
    """
    Query the databse from a table of tweets. 
    """
    engine = create_engine("postgresql+psycopg2://%s:%s@%s:%d/%s" %(usertwitter, passwordtwitter, hosttwitter, porttwitter, dbnametwitter))
    table = pd.read_sql_query("select * from %s" %tabletweets,con=engine, index_col="id")
    return table

def preprocessing_text(table):
    """
    Preprocess the tweets by putting them in an easy-to-understand format. 
    This means getting rid of links, blanks, etc.
    """
    # Put everythin in lowercase.
    table["tweet"] = table["tweet"].str.lower()
    # Replace rt indicating that was a retweet.
    table["tweet"] = table["tweet"].str.replace("rt", "")
    # Replace occurences of mentioning @UserNames.
    table["tweet"] = table["tweet"].replace(r"@\w+", "", regex=True)
    # Replace links contained in the tweet.
    table["tweet"] = table["tweet"].replace(r'http\S+', "", regex=True)
    table["tweet"] = table["tweet"].replace(r'www.[^ ]+', "", regex=True)
    # Remove numbers.
    table["tweet"] = table["tweet"].replace(r'[0-9]+', "", regex=True)
    # Replace special characters and puntuation marks.
    table["tweet"] = table["tweet"].replace(r'[!'#$%&()*+,-./:;<=>?@[\]^_`{|}~]', "", regex=True)
    return table

def in_dict(word):
    """
    Keep the words that are based off other words as the base words they're
    made off of.
    """
    if wordnet.synsets(word):
        # If the word is in the dictionary, we'll return True.
        return True

def replace_elongated_word(word):
    regex = r'(\w*)(\w+)\2(\w*)'
    repl = r'\1\2\3'    
    if in_dict(word):
        return word
    new_word = re.sub(regex, repl, word)
    if new_word != word:
        return replace_elongated_word(new_word)
    else:
        return new_word

def detect_elongated_words(row):
    """
    Find the long ones.
    """
    regexrep = r'(\w*)(\w+)(\2)(\w*)'
    words = ["".join(i) for i in re.findall(regexrep, row)]
    for word in words:
        if not in_dict(word):
            row = re.sub(word, replace_elongated_word(word), row)
    return row


def stop_words(table):
    """
    We need to remove the stop words. These are the prepositions, small words, etc., that
    don't give us more info.
    """
    stop_words_list = stopwords.words("english")
    table["tweet"] = table["tweet"].str.lower()
    table["tweet"] = table["tweet"].apply(lambda x: " ".join([word for word in x.split() if word not in (stop_words_list)]))
    return table

def replace_antonyms(word):
    """
    We get all the lemma for the word.
    """
    for syn in wordnet.synsets(word): 
        for lemma in syn.lemmas(): 
            #if the lemma is an antonyms of the word
            if lemma.antonyms(): 
                #we return the antonym
                return lemma.antonyms()[0].name()
    return word
            
def handling_negation(row):
    """
    Tokenize the row.
    """
    words = word_tokenize(row)
    speach_tags = ["JJ", "JJR", "JJS", "NN", "VB", "VBD", "VBG", "VBN", "VBP"]
    #We obtain the type of words that we have in the text, we use the pos_tag function
    tags = nltk.pos_tag(words)
    #Now we ask if we found a negation in the words
    tags_2 = ""
    if "n't" in words and "not" in words:
        tags_2 = tags[min(words.index("n't"), words.index("not")):]
        words_2 = words[min(words.index("n't"), words.index("not")):]
        words = words[:(min(words.index("n't"), words.index("not")))+1]
    elif "n't" in words:
        tags_2 = tags[words.index("n't"):]
        words_2 = words[words.index("n't"):] 
        words = words[:words.index("n't")+1]
    elif "not" in words:
        tags_2 = tags[words.index("not"):]
        words_2 = words[words.index("not"):]
        words = words[:words.index("not")+1] 
    for index, word_tag in enumerate(tags_2):
        if word_tag[1] in speach_tags:
            words = words+[replace_antonyms(word_tag[0])]+words_2[index+2:]
            break
    return " ".join(words)

def cleaning_table(table):
    """
    This function will process all the required cleaning for the text in our tweets.
    """
    table = preprocessing_text(table)
    table["tweet"] = table["tweet"].apply(lambda x: detect_elongated_words(x))
    table["tweet"] = table["tweet"].apply(lambda x: handling_negation(x))
    table = stop_words(table)
    return table

def vectorization(table):
    """
    Vectorize the table into a format that can be visualized.
    This lets pandas and matplotlib create visuals that can be stretched
    and fitted.
    """
    # CountVectorizer will convert a collection of text documents to a matrix of token counts.
    # Produces a sparse representation of the counts.
    # Initialize.
    vector = CountVectorizer()
    # We fit and transform the vector created.
    frequency_matrix = vector.fit_transform(table.tweet)
    # Sum all the frequencies for each word.
    sum_frequencies = np.sum(frequency_matrix, axis=0)
    # Now we use squeeze to remove single-dimensional entries 
    # from the shape of an array that we got from applying 
    # np.asarray to the sum of frequencies.
    frequency = np.squeeze(np.asarray(sum_frequencies))
    # Now we get into a dataframe all the frequencies 
    # and the words that they correspond to.
    frequency_df = pd.DataFrame([frequency], columns=vector.get_feature_names()).transpose()
    return frequency_df

def word_cloud(tweets):
    """
    Create the word cloud.
    """
    file = os.getcwd()
    # We read the mask image into a numpy array.
    anime_mask = np.array(Image.open(os.path.join(file, "anime.png")))
    # Now we store the tweets into a series to be able to process.
    #tweets_list = pd.Series([t for t in tweet_table.tweet]).str.cat(sep=" ") 
    # We generate the wordcloud using the series created and the mask.
    wc = WordCloud(width=2000, height=1000, max_font_size=200, background_color="black", max_words=2000, mask=anime_mask, contour_width=1, 
                           contour_color="steelblue", colormap="nipy_spectral", stopwords=["anime"])
    wc.generate(tweets)
    # wordcloud = WordCloud(width=1600, height=800,max_font_size=200).generate(tweets_list)
    # Now we plot both figures, the wordcloud and the mask
    plt.figure(figsize=(10,10))
    plt.imshow(wc, interpolation="hermite")
    plt.axis("off")
    # plt.imshow(anime_mask, cmap=plt.cm.gray, interpolation="bilinear")
    # plt.axis("off")    
    plt.show()

def wfgraph(wf, sent):
    """
    Create a network graph of word frequency wf.
    """
    labels = wf[0][1:51].index
    title = ("Word Frequency for %s" %sent)
    # Plot.
    plt.figure(figsize=(10,5))
    plt.bar(np.arange(50), wf[0][1:51], width = 0.8, color = sns.color_palette("bwr"), alpha=0.5, 
            edgecolor = "black", capsize=8, linewidth=1)
    plt.xticks(np.arange(50), labels, rotation=90, size=14)
    plt.xlabel("50 more frequent words", size=14)
    plt.ylabel("Frequency", size=14)
    # plt.title(("Word Frequency for %s", size=18) % sent)
    plt.title(title, size=18)
    plt.grid(False)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.show()


def regression_graph(table):
    """
    Use regression to graph the table and separate it into the 
    underlying factors that cause the tweets and data.
    """
    table = table[1:]
    # Plot.
    sns.set_style("whitegrid")   
    plt.figure(figsize=(6,6))
    points = plt.scatter(table["Positive"], table["Negative"], c=table["Positive"], s=75, cmap="bwr")
    plt.colorbar(points)
    sns.regplot(x="Positive", y="Negative",fit_reg=False, scatter=False, color=".1", data=table)
    plt.xlabel("Frequency for Positive Tweets", size=14)
    plt.ylabel("Frequency for Negative Tweets", size=14)
    plt.title("Word frequency in Positive vs. Negative Tweets", size=14)
    plt.grid(False)
    sns.despine()

def splitting(table):
    """
    Split the data into training and test datasets.
    """
    X_train, X_test, y_train, y_test = train_test_split(table.tweet, table.sentiment, test_size=0.2, shuffle=True)
    return X_train, X_test, y_train, y_test
