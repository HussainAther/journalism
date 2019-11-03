import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapefile

"""
Critical mineral graphs
"""

# # Read in shapefile
# shape = shapefile.Reader("data/criticalminerals/PP1802_CritMin_pts.shp") 

# # First feature of the shapefile
# feature = shape.shapeRecords()[0]
# first = feature.shape.__geo_interface__  
# print(first) # (GeoJSON format)

# Use geopandas to read in shapefile as DataFrame. 
gdf = gpd.read_file("data/criticalminerals/PP1802_CritMin_pts.shp")

# Read in world file.
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
# geoplot.polyplot(world, figsize=(8, 4))

# Plot.
ax = world.plot(color="white", edgecolor="black")
gdf.plot(ax=ax, color="red", markersize=3)
plt.savefig("output/criticalminerals/worldmap.png")
plt.close()

# Restrict to North America.
ax = world[world.continent == "North America"].plot(
    color="white", edgecolor="black")
nagdf = pd.concat([gdf.loc[gdf["LOCATION"] == "United States of America"], 
                  gdf.loc[gdf["LOCATION"] == "Canada"],
                  gdf.loc[gdf["LOCATION"] == "Mexico"]])
nagdf.plot(ax=ax, color="red", markersize=2)

# Plot.
plt.savefig("output/criticalminerals/namap.png")

print(gdf["CRITICAL_M"])
