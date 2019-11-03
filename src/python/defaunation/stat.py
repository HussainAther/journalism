import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import researchpy

"""
Defaunation statistics
"""

# Tranpose the input DataFrame.
df = pd.DataFrame.from_csv("data/defaunation/gardneretal.csv", encoding="windows-1252")

print(df.head())
print(df.loc[df["Region"] == "Neotropics"])
print(df.columns)
# researchpy.ttest(df.loc[df["Region"] == "Neotropics"], df.loc[df["Region"] == "Africa"])

