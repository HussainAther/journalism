import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# K-Nearest neighbors clustering (kNN) with
# greater circle distance as a metric to minimize.
# Also kd-tree (kd tree kdtree).

def valpoint(p):
    """
    Validate a point.
    """
    lat, lon = p
    assert -90 <= lat <= 90, "bad latitude"
    assert -180 <= lon <= 180, "bad longitude"

def distance_haversine(a):
    """
    Calculate the great circle distance between two lists of 
    latitudes and longitudes of points 
    on the earth (specified in decimal degrees). 
    Haversine
    formula: 
        a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
        c = 2 ⋅ atan2( √a, √(1−a) )
        d = R ⋅ c
    where   φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371km);
            note that angles need to be in radians to pass to trig functions!
    """
    lat, lon = a 
    for p in zip(lat, lon):
        valpoint(p)
    R = 6371 # km - earths's radius
    # convert decimal degrees to radians 
    lat, lon = map(np.radians, [lat, lon])
    # haversine formula 
    dlon, dlat = np.diff(lon), np.diff(lat)
    print(dlon)
    np.insert(dlon, 0)
    np.insert(dlat, 0)
    f = np.sin(dlat/2)**2 + np.cos(lat) * np.cos(lat) * np.sin(dlon/2)**2
    c = 2 * np.asin(np.sqrt(f)) # 2 * np.atan2(np.sqrt(f), np.sqrt(1-f))
    d = R * c
    return d

distances = distance_haversine((magdf["latitude"], magdf["longitude"]))
