import nltk
from wordcloud import WordCloud
nltk.download("stopwords")

WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color="steelblue").generate_from_text(" ".join([r for r in open("mobydick.txt", "r").read().split() if r not in set(nltk.corpus.stopwords.words("english"))])).to_file("wordcloud.png")