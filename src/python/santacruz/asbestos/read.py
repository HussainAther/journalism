import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

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

# Save to file.
crs = {"init": "epsg:2263"} #http://www.spatialreference.org/ref/epsg/2263/
gdf = gpd.GeoDataFrame(df, crs=crs, geometry=geom)
gdf.to_file(driver="ESRI Shapefile", filename="output/asbestos/data")

# Restrict to America.
country = gpd.read_file("data/gz_2010_us_040_00_5m.json")
country = country[country["NAME"].isin(["Alaska","Hawaii"]) == False]

# Plot.
ax = country.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/asbestos/usmap.png")

# Close.
plt.close()

# Restrict to California.
ca = country[country["NAME"].isin(["California"]) == True]
df = df.loc[df["state"] == "CA"]
geom = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
gdf = gpd.GeoDataFrame(
    df, geometry=geom)

# Plot.
ax = ca.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/asbestos/california.png")

