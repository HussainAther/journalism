import chart_studio.plotly as py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

from collections import OrderedDict
from itertools import cycle, islice
from matplotlib.dates import DateFormatter

"""
Use pandas to analyze the UCSC Science Communication Class of 2020 
slack usage during the fall quarter and visualize as interactive graphs
with plotly.
"""

# Read in the data and select only the dates of the fall quarter.
df = pd.read_csv("data/slack/ucscscicom20fall.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create a column of each day of the week.
dow = ["M", "T", "W", "H", "F", "Sa", "Su"]
daylist = []
for i in df["Date"].dt.dayofweek.values:
    daylist.append(dow[i])
df["Day of the week"] = daylist

# Change the date to a more reader-friendly format.
# df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.strftime("%m-%d")

# Get only the fall quarter dates.
mask = (df["Date"] >= "2019-09-30") & (df["Date"] <= "2019-12-13")
df = df.loc[mask]

# Convert the number of messages posted from a string to an integer, if it isn't already.
df["Messages posted"] = df["Messages posted"].astype(int)

# Keep track of each message posted on that day,
# not the total number of messages so far.
dailymessages = []
prev = 288
for index, value in enumerate(df["Messages posted"]):
    dailymessages.append(value-prev)
    prev = value

df["Messages sent"] = dailymessages

# Get the data we need.
graphdata = pd.concat([df["Date"], df["Messages sent"], df["Day of the week"]], axis=1)

# Plot.
fig = px.bar(graphdata, x="Date", y="Messages sent",
       hover_data=["Messages sent", "Day of the week"], color="Day of the week")

fig.update_yaxes(range=[1, 225])
fig.update_layout(title="Fall quarter UCSC Sci Com Slack Usage")

fig.show()
py.plot(fig)
