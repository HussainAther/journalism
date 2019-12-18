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
