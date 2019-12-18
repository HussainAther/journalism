import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import re

from operator import itemgetter

"""
Create an interactive network of how distant Twitter
followers are from one another.
"""

pd.set_option("display.float_format", lambda x: "%.f" % x)

# Read JSON into a pandas DataFrame.
df = pd.read_json("tweets.txt")

# Get the info we want.
eqcol = ["created_at", "id", "text"]
final[eqcol] = df[eqcol]

def getbasics(tfinal):
    """
    Get the basic information about the user.
    """
    tfinal["screen_name"] = tweets_df["user"].apply(lambda x: x["screen_name"])
    tfinal["user_id"] = tweets_df["user"].apply(lambda x: x["id"])
    tfinal["followers_count"] = tweets_df["user"].apply(lambda x: x["followers_count"])
    return tfinal

def getusermentions(tfinal):
    """
    Get user mentions.
    """
    # Inside the tag "entities" will find "user mentions" and will get "screen name" and "id"
    tfinal["user_mentions_screen_name"] = tweets_df["entities"].apply(lambda x: x["user_mentions"][0]["screen_name"] if x["user_mentions"] else np.nan)
    tfinal["user_mentions_id"] = tweets_df["entities"].apply(lambda x: x["user_mentions"][0]["id_str"] if x["user_mentions"] else np.nan)
    return tfinal
