import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

"""
Visualize the quadranagle of magnetic activity for the Santa Cruz area.
"""

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

print(magdf.loc[magdf["diurnal"] == 50399.8])

# Plot.
plot = sns.lmplot("latitude", "longitude", data=magdf, fit_reg=False, hue="diurnal", legend=False)
plot.savefig("output/santacruz/airborne/quadrangle.png")

