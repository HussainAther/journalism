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
tfinal = pd.DataFrame(columns = ["created_at", "id", "in_reply_to_screen_name", 
                                       "in_reply_to_status_id", "in_reply_to_user_id",
                                       "retweeted_id", "retweeted_screen_name", "user_mentions_screen_name", 
                                       "user_mentions_id", "text", "user_id", "screen_name", "followers_count"])
eqcol = ["created_at", "id", "text"]
tfinal[eqcol] = df[eqcol]

def getbasics(tfinal):
    """
    Get the basic information about the user.
    """
    tfinal["screen_name"] = df["user"].apply(lambda x: x["screen_name"])
    tfinal["user_id"] = df["user"].apply(lambda x: x["id"])
    tfinal["followers_count"] = df["user"].apply(lambda x: x["followers_count"])
    return tfinal

def getusermentions(tfinal):
    """
    Get user mentions.
    """
    # Inside the tag "entities" will find "user mentions" and will get "screen name" and "id"
    tfinal["user_mentions_screen_name"] = df["entities"].apply(lambda x: x["user_mentions"][0]["screen_name"] if x["user_mentions"] else np.nan)
    tfinal["user_mentions_id"] = df["entities"].apply(lambda x: x["user_mentions"][0]["id_str"] if x["user_mentions"] else np.nan)
    return tfinal

def getretweets(tfinal):
    """
    Get retweets.
    """
    # Inside the tag "retweeted_status" will find "user" and will get "screen name" and "id". 
    tfinal["retweeted_screen_name"] = df["retweeted_status"].apply(lambda x: x["user"]["screen_name"] if x is not np.nan else np.nan)
    tfinal["retweeted_id"] = df["retweeted_status"].apply(lambda x: x["user"]["id_str"] if x is not np.nan else np.nan)
    return tfinal

def getinreply(tfinal):
    """
    Get reply info.
    """
    # Just copy the 'in_reply' columns to the new dataframe
    tfinal["in_reply_to_screen_name"] = df["in_reply_to_screen_name"]
    tfinal["in_reply_to_status_id"] = df["in_reply_to_status_id"]
    tfinal["in_reply_to_user_id"]= df["in_reply_to_user_id"]
    return tfinal

def filldf(tfinal):
    """
    Put it all together.
    """
    getbasics(tfinal)
    getusermentions(tfinal)
    # getretweets(tfinal)
    # getinreply(tfinal)
    return tfinal

def getinteractions(row):
    """
    Get the interactions between different users.
    """
    # From every row of the original DataFrame.
    # First we obtain the "user_id" and "screen_name".
    user = row["user_id"], row["screen_name"]
    # Be careful if there is no user id
    if user[0] is None:
        return (None, None), []
    
    # The interactions are going to be a set of tuples.
    interactions = set()
    
    # Add all interactions. 
    # First, we add the interactions corresponding to replies adding the id and screen_name.
    interactions.add((row["in_reply_to_user_id"], row["in_reply_to_screen_name"]))
    # After that, we add the interactions with retweets.
    interactions.add((row["retweeted_id"], row["retweeted_screen_name"]))
    # And later, the interactions with user mentions.
    interactions.add((row["user_mentions_id"], row["user_mentions_screen_name"]))
    
    # Discard if user id is in interactions.
    interactions.discard((row["user_id"], row["screen_name"]))
    # Discard all not existing values.
    interactions.discard((None, None))
    # Return user and interactions.
    return user, interactions

tfinal = filldf(tfinal)

