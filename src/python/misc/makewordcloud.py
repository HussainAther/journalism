import nltk
import os
import sys

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize 
from wordcloud import WordCloud

"""
Create a word cloud from an input file of text and an option
image of a shape to use as the mask for the word cloud.

Usage: `python inputfile maskimage`
"""

# Stopwords used to remove unnecessary words from text
en_stop = nltk.download("stopwords")
stopwords = set(stopwords.words("english"))

# Get the user input.
tf = sys.argv[1] # textfile
if len(sys.argv) == 2:
    mi = None
elif len(sys.argv) == 3:
    mi = sys.argv[2] 

# Read in the file and use stopwords to filter out 
# key words from the other text.
file1 = open(tf, "r") 
line = file1.read() # Use this to read file content as a stream. 
words = line.split()
wordstring = "" 
for r in words: 
    if not r in stopwords: 
        wordstring += r + " "  

# Create wordcloud.
wc = WordCloud(background_color="white", 
               max_words=5000, 
               contour_width=3, 
               contour_color="steelblue", 
               mask=mi)
wcimg = wc.generate_from_text(wordstring)
wcimg.to_file("output/" + tf + "_wordcloud.png")
print("Wordcloud created.")
