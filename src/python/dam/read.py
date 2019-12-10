import pandas as pd

"""
Read in and analyze the Oregon dam data.
"""

df = pd.read_csv("data/dam/oregondams.csv")

print(df.head)
