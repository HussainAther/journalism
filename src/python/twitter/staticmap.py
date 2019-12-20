import json
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import pandas as pd
import re
import sys

from operator import itemgetter

"""
Create a network of how distant Twitter
followers are from one another.
"""

pd.set_option("display.float_format", lambda x: "%.f" % x)

# Read input JSON file.
tweetsjson = sys.argv[1]

# Read JSON into a pandas DataFrame.
df = pd.read_json(tweetsjson)

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
    # getusermentions(tfinal)
    getretweets(tfinal)
    getinreply(tfinal)
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
tfinala = tfinal.where((pd.notnull(tfinal)), None)

def getinteractions(row):
    """
    Get the interactions between different users.
    """
    # From every row of the original dataframe
    # First we obtain the "user_id" and "screen_name".
    user = row["user_id"], row["screen_name"]
    # Be careful if there is no user id
    if user[0] is None:
        return (None, None), []
    
    # The interactions are going to be a set of tuples.
    interactions = set()
    
    # Add all interactions.
    # First, we add the interactions corresponding to replies adding the id and screen_name
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

# Get graph information.
degrees = [val for (node, val) in graph.degree()]
print("The maximum degree of the graph is " + str(np.max(degrees))) 
print("The minimum degree of the graph is " + str(np.min(degrees)))
print("There are " + str(graph.number_of_nodes()) + " nodes and " + str(graph.number_of_edges()) + " edges present in the graph")
print("The average degree of the nodes in the graph is " + str(np.mean(degrees))) 

if nx.is_connected(graph):
    print("The graph is connected")
else:
    print("The graph is not connected")
print("There are " + str(nx.number_connected_components(graph)) + " connected in the graph.")

largestsubgraph = max(nx.connected_component_subgraphs(graph), key=len)
print("There are " + str(largestsubgraph.number_of_nodes()) + " nodes and " + str(largestsubgraph.number_of_edges()) + " edges present in the largest component of the graph.")

if nx.is_connected(largestsubgraph):
    print("The graph is connected")
else:
    print("The graph is not connected")

print("The average clustering coefficient is " + str(nx.average_clustering(largestsubgraph)) + " in the largest subgraph")
print("The transitivity of the largest subgraph is " + str(nx.transitivity(largestsubgraph)))
print("The diameter of our graph is " + str(nx.diameter(largestsubgraph)))
print("The average distance between any two nodes is " + str(nx.average_shortest_path_length(largestsubgraph)))

graphcentrality = nx.degree_centrality(largestsubgraph)
maxde = max(graphcentrality.items(), key=itemgetter(1))
graphcloseness = nx.closeness_centrality(largestsubgraph)
graphbetweenness = nx.betweenness_centrality(largestsubgraph, normalized=True, endpoints=False)
maxclo = max(graphcloseness.items(), key=itemgetter(1))
maxbet = max(graphbetweenness.items(), key=itemgetter(1))

print("The node with ID " + str(maxde[0]) + " has a degree centrality of " + str(maxde[1]) + " which is the max of the graph.")
print("The node with ID " + str(maxclo[0]) + " has a closeness centrality of " + str(maxclo[1]) + " which is the max of the graph.")
print("The node with ID " + str(maxbet[0]) + " has a betweenness centrality of " + str(maxbet[1]) + " which is the max of the graph.")

pos = nx.spring_layout(largestsubgraph, k=0.05)

nodeanddegree = largestsubgraph.degree()
centralnodes = list(set([maxde[0], maxclo[0], maxbet[0]]))
centralnodescolors = [] 
colors = ["b", "g", "r", "c", "m", "y", "k", "w"]
for i in range(len(centralnodes)):
    if i == 8:
        centralnodescolors.append("b")  
    else:
        centralnodescolors.append(colors[i])

# Networkx static image
fig = nx.draw(largestsubgraph)
plt.figure(figsize = (20,20))
nx.draw(largestsubgraph, 
        pos=pos, 
        cmap=plt.cm.PiYG) 

nx.draw_networkx_nodes(largestsubgraph, 
                       pos=pos, 
                       nodelist=centralnodes, 
                       node_size=300, 
                       node_color=centralnodescolors)
filename = tweetsjson.split("/")[-1].replace(".json", "")
plt.savefig("output/twitter/" + filename + ".png")
plt.close()
