import numpy as np
import pandas as pd

"""
Read and analyze the FOIA data.
"""

df = pd.read_csv("data/foia/foiacontacts.csv")
print(df.columns)
