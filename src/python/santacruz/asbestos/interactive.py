import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

from shapely.geometry import Point

"""
Let's get down to business to defeat asbestos.
"""

px.set_mapbox_access_token(open(".mapbox_token").read())

# Read data.
df = pd.read_csv("data/santacruz/asbestos/main.csv")

# Extract data.
geom = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
gdf = gpd.GeoDataFrame(
    df, geometry=geom)

# Restrict to America.
country = gpd.read_file("data/gz_2010_us_040_00_5m.json")
country = country[country["NAME"].isin(["Alaska","Hawaii"]) == False]

# Plot.
fig, ax = plt.subplots()
px.scatter_mapbox(gdf, lat="latitude", lon="longitude", hover_data=["county", "state"]) 
fig.show()

