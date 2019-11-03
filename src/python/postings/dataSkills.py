import csv
import os
import pandas as pd

"""
Usage: "python dataskills.py"
Use a scaffolding on competencies through various domains of data management. This is based
on existing research in data management skills.
"""

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while os.getcwd().split("/")[-1] != "journalism":
    os.chdir("..")

# Check if the output file directory exists. If not, make it.
if not os.path.isdir("output/skills"):
    os.mkdir("output/skills")

# Input the .csv as a pandas DataFrame.
df = pd.read_csv("data/skills/skills.csv")
