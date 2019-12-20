import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sys
import urllib2

"""
Create an interactive network of how distant Twitter
followers are from one another.
"""

# Read input JSON file.
data = sys.argv[1]

# Read JSON into a pandas DataFrame.
df = pd.read_json(tweetsjson)

# Initialize the network graph.
graph = nx.Graph()

for index, tweet in tfinal.iterrows():
    user, interactions = getinteractions(tweet)
    user_id, user_name = user
    tweet_id = tweet["id"]
    for interaction in interactions:
        int_id, int_name = interaction
        graph.add_edge(user_id, int_id, tweet_id=tweet_id)
        graph.node[user_id]["name"] = user_name
        graph.node[int_id]["name"] = int_name

