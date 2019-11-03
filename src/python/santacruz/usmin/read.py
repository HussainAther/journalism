import shapefile
import numpy as np
import geopandas as gpd

import matplotlib.pyplot as plt

fp = "data/santacruz/usmin/poly.shp"

gdf = gpd.read_file(fp, encoding="utf-8") 

# Restrict to America.
country = gpd.read_file("data/gz_2010_us_040_00_5m.json")
country = country[country["NAME"].isin(["Alaska","Hawaii"]) == False]

# Plot.
ax = country.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/santacruz/usmin/usmap.png")

# Close.
plt.close()

# Restrict to California.
ca = country[country["NAME"].isin(["California"]) == True]
cagdf = gdf.loc[gdf["STATE"] == "CA"]
gdf = gpd.GeoDataFrame(
    cagdf, geometry=ca["geometry"])

# Plot.
ax = ca.plot(color="white", edgecolor="black")
cagdf.plot(ax=ax, color="red")

# Save.
plt.savefig("output/santacruz/usmin/california.png")
