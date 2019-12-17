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
