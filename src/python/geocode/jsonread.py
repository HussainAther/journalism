import geopandas as gpd
import json

"""
Read in the geocoding file.
"""

with open("data/geocode/refine_geocoder.json") as f:
    data = json.load(f)

