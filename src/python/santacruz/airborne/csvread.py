import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from clustergrammer import Network

"""
Visualize the quadrangle of magnetic activity for the Santa Cruz area.
"""

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# Plot.
plot = sns.lmplot("latitude", "longitude", data=magdf, fit_reg=False, hue="diurnal", legend=False)
plot.savefig("output/santacruz/airborne/quadrangle.png")

"""
Make an interactive map.
"""

# Initialize.
net = Network()

# Load the file.
net.load_file("data/santacruz/airborne/magsimple.tsv")

net.cluster(enrichrgram=False)

net.widget()
