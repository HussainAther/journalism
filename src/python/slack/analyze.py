import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from collections import OrderedDict

"""
Use pandas to analyze the UCSC Science Communication Class of 2020 
slack usage during the fall quarter and visualize.
"""

# Read in the data and select only the dates of the fall quarter.
df = pd.read_csv("data/slack/ucscscicom20fall.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Create a column of each day of the week.
dow = ["M", "T", "W", "H", "F", "Sa", "Su"]
daylist = []
for i in df["Date"].dt.dayofweek.values:
    daylist.append(dow[i])
df["dow"] = daylist

# Change the date to a more reader-friendly format.
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.strftime("%m-%d")

# Get only the fall quarter dates.
mask = (df["Date"] >= "09-30") & (df["Date"] <= "12-13")
df = df.loc[mask]


# Convert the number of messages posted from a string to an integer, if it isn't already.
df["Messages posted"] = df["Messages posted"].astype(int)

dailymessages = []
prev = 304
for index, value in enumerate(df["Messages posted"]):
    dailymessages.append(value-prev)
    prev = value

df["dm"] = dailymessages

# Dictionary of colors for each day of the week
daydict = {"M" : "#FF0000", 
           "T" : "#FF7F00", 
           "W" : "#FFFF00", 
           "H" : "#00FF00", 
           "F" : "#0000FF", 
           "Sa" : "#2E2B5F", 
           "Su" : "#8B00FF"}

# Plot.
fig, ax = plt.subplots()
for index, value in enumerate(df["dm"]):
    dow = df.iloc[index]["dow"]
    plt.bar(index, value, color=daydict[dow], label=dow, tick_label=index)

# Label.
ax.legend(loc="best")
ax.set_xlabel("Date")
ax.set_ylabel("Slack messages")
ax.set_title("UCSC SciCom 2020 Slack Usage")

# Add legend
handles, labels = ax.get_legend_handles_labels()
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), loc=2)

# Save.
plt.savefig("output/slack/postfreqfall.png")
