import pandas as pd

"""
Read in Medicare data.
"""

df = pd.read_csv("data/medicare/CA_counties_medicare.csv")
print(df.columns)
