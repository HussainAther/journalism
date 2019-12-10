import matplotlib.pyplot as plt
import pandas as pd

"""
Read in and analyze the Oregon dam data.
"""

df = pd.read_csv("data/dam/oregondams.csv")
cfreqs = df["county"].value_counts() # frequency of each county
cindex = df["county"].value_counts().index # county name

plt.bar(cindex, cfreqs)
plt.xticks(range(len(cindex)), cindex, rotation="vertical")
plt.xlabel("County")
plt.ylabel("Number of dams")
plt.title("Dam frequency by county")
plt.savefig("output/dam/freq.png")
