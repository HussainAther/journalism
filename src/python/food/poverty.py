import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Analyze poverty data from the Income and Poverty in the United States: 2016
report.
"""

# Read each .csv file as a pandas DataFrame.
allraces = pd.read_csv("data/food/poverty/allraces.csv")
aa = pd.read_csv("data/food/poverty/asianalone.csv")
aaoic = pd.read_csv("data/food/poverty/asianaloneorincombination.csv")
aapi = pd.read_csv("data/food/poverty/asianandpacificislander.csv")
b = pd.read_csv("data/food/poverty/black.csv")
ba = pd.read_csv("data/food/poverty/blackalone.csv")
baoic = pd.read_csv("data/food/poverty/blackaloneorincombination.csv")
har = pd.read_csv("data/food/poverty/hispanicanyrace.csv")
w = pd.read_csv("data/food/poverty/white.csv")
wa = pd.read_csv("data/food/poverty/whitealone.csv")
wanh = pd.read_csv("data/food/poverty/whitealonenothispanic.csv")
wnh = pd.read_csv("data/food/poverty/whitenothispanic.csv")

# List of the DataFrames
dflist = [allraces, aa, aaoic, aapi, b, ba, baoic, har, w, wa, wanh, wnh]

fig = plt.figure()
ax = plt.axes()
for df in dflist:
#    plt.plot(df["All people (Total)"])
