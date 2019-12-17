import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize 
from wordcloud import WordCloud
en_stop = nltk.download("stopwords")
WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color="steelblue").generate_from_text(" ".join([r for r in open("mobydick.txt", "r").read().split()] if r not in set(stopwords.words("english"))).to_file("sys.argv[1] + "_wordcloud.png")
