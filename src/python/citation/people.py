import pandas as pd
import os

"""
This file has example pandas usage.
"""

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while os.getcwd().split("/")[-1] != "journalism":
    os.chdir("..")

# Use the read_csv function to open up the .csv containing 
# information about people.
df = pd.read_csv("data/people/people.csv")
df.info()

# Print the first names of each person.
print(df["fname"])

# Print the people older than 33.
print(df["age"] > 33)
