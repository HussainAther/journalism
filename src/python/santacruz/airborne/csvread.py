import chart_studio.plotly as py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import seaborn as sns

from clustergrammer import Network

"""
Visualize the quadrangle of magnetic activity for the Santa Cruz area.
"""

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

print("Magnetic field")
print("Minimum: ", min(magdf["diurnal"]))
print("Maximum: ", max(magdf["diurnal"]))

# Plot.
plot = sns.lmplot("latitude", "longitude", data=magdf, fit_reg=False, hue="diurnal", legend=False)
plot.savefig("output/santacruz/airborne/quadrangle.png")

"""
Make an interactive map with clustergrammar.

# Initialize.
net = Network()

# Load the file.
net.load_file("data/santacruz/airborne/magsimple.tsv")

net.cluster(enrichrgram=False)

net.widget()
"""

"""
Make an interactive map with plotly.
"""

# Load the file.
simplemagdf = pd.read_csv("data/santacruz/airborne/magsimplecut.csv")
# magdfmatrix = simplemagdf.pivot("latitude", "longitude", "diurnal")

# Get the magnetic field as a float.
mf = simplemagdf["diurnal"].astype(float)

# Set the color scale.
colorscale = [[50375, "#edf8fb"], [50383.5, "#b3cde3"],  [50391.5, "#8856a7"],  [50399, "#810f7c"]]

# Plot.
heatmap = go.Heatmap(z=simplemagdf["diurnal"], 
                     x=simplemagdf["latitude"], 
                     y=mf)
#                     colorscale=colorscale)
data = [heatmap]
py.iplot(data, filename="airborneheatmap.html")

