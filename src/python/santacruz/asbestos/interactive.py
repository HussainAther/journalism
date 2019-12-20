import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

from shapely.geometry import Point

"""
Let's get down to business to defeat asbestos.
"""

# Read data.
df = pd.read_csv("data/asbestos/main.csv")

# Extract data.
geom = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
gdf = gpd.GeoDataFrame(
    df, geometry=geom)
print(gdf)

fig = px.scatter_mapbox(gdf, lat="latitude", lon="longitude") 
