import chart_studio.plotly as py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import seaborn as sns

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
Make an interactive map with plotly.

# Load the file.
simplemagdf = pd.read_csv("data/santacruz/airborne/magsimple.csv")
# magdfmatrix = simplemagdf.pivot("latitude", "longitude", "diurnal")

# Get the magnetic field as a float.
simplemagdf["diurnal"] = simplemagdf["diurnal"].astype(float)

# Cut the data for plotly size constraints.
simplemagdf = simplemagdf[(simplemagdf["latitude"] >= 36.4) & (simplemagdf["latitude"] <= 36.6)]
simplemagdf = simplemagdf[(simplemagdf["longitude"] >= -121.5) & (simplemagdf["longitude"] <= -120.5)]

# Create figure.
fig = go.Figure()

fig.add_trace(
    go.Scattergl(
        x = simplemagdf["longitude"],
        y = simplemagdf["latitude"],
        mode = "markers",
        marker = dict(
                color=simplemagdf["diurnal"],
                colorscale="Viridis"),
        hovertext=[simplemagdf["latitude"], 
                    simplemagdf["longitude"],
                    simplemagdf["diurnal"]],
        showlegend=True
    )
)

fig.update_layout(title="Magnetic field (nT) across Santa Cruz")
py.plot(fig)
