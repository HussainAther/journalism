import json

"""
Read in the geocoding file.
"""

with open("data/src/geocode/refine_geocoder.json") as f:
    data = json.load(f)

