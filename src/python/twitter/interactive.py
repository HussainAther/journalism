import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sys
import urllib2

from plotly.offline import iplot, plot

"""
Create an interactive network of how distant Twitter
followers are from one another using tweets.
"""

# Read input JSON file.
inputjson = sys.argv[1]

# Read JSON into a pandas DataFrame.
df = pd.read_json(inputjson)

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

# Plot.
# Get the edges.
Xe=[]
Ye=[]
for e in G.edges():
    Xe.extend([pos[e[0]][0], pos[e[1]][0], None])
    Ye.extend([pos[e[0]][1], pos[e[1]][1], None])

# Trace.
trace_nodes=dict(type="scatter",
                 x=Xn, 
                 y=Yn,
                 mode="markers",
                 marker=dict(size=28, color="rgb(0,240,0)"),
                 text=labels,
                 hoverinfo="text")
trace_edges=dict(type="scatter",                  
                 mode="lines",                  
                 x=Xe,                  
                 y=Ye,                 
                 line=dict(width=1, color="rgb(25,25,25)"), hoverinfo="none")

# Use the Fruchterman Reingold (Fruchterman-Reingold) layout algorithm to plot.
axis=dict(showline=False, 
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=""
          )
layout=dict(title= "My Grapha",  
             font= dict(family="Balto"),
             width=600,
             height=600,
             autosize=False,
             showlegend=False,
             xaxis=axis,
             yaxis=axis,
             margin=dict(
             l=40,
             r=40,
             b=85,
             t=100,
             pad=0,   
     ),
     hovermode="closest",
     plot_bgcolor="#EFECEA", #set background color            
     )
fig = dict(data=[trace_edges, trace_nodes], layout=layout)
def make_annotations(pos, anno_text, font_size=14, font_color='rgb(10,10,10)'):
    L=len(pos)
    if len(anno_text)!=L:
        raise ValueError("The lists pos and text must have the same len")
    annotations = []
    for k in range(L):
        annotations.append(dict(text=anno_text[k], 
                                x=pos[k][0], 
                                y=pos[k][1]+0.075, # This additional value is chosen by trial and error
                                xref="x1", yref="y1",
                                font=dict(color= font_color, size=font_size),
                                showarrow=False)
                          )
    return annotations  
fig["layout"].update(annotations=make_annotations(pos, labels))
iplot(fig)