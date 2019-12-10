import matplotlib.pyplot as plt
import pandas as pd

"""
Read in and analyze the Oregon dam data.
"""

df = pd.read_csv("data/dam/oregondams.csv")

plt.bar(df["county"].value_counts())
