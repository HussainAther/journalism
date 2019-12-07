import pandas as pd

"""
Read the FOIA data.
"""

df = pd.read_csv("data/foia/foiacontacts.csv")
print(df.head)
