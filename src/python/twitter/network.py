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
Visualizing Twitter followers.
"""

