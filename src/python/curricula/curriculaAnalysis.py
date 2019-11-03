import re
import glob
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

"""
Analysis of Data Science curricula among higher institutions of learning.

Usage: "python curanalysis.py"

Use the curricula .csv files in the data/curricula directory as input files. 
"""

# Each curricula .csv file in list of dictionary format
# that we will convert to a pandas DataFrame
curfiles = []

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while os.getcwd().split("/")[-1] != "journalism":
    os.chdir("..")

abbrevdict = {
    "BROWN" : "Brown",
    "CALT" : "CalTech",
    "COLNY" : "Columbia",
    "GTOWN" : "Georgetown",
    "HRVRD" : "Harvard",
    "MARQ" : "Marquette",
    "MIT" : "MIT",
    "NCSU" : "NC State",
    "NU": "Northwestern",
    "NYU" : "NYU",
    "OHIO" : "Ohio State",
    "PURD" : "Purdue",
    "RICE" : "Rice",
    "RUTG" : "Rutgers",
    "STAN" : "Stanford",
    "UCB" : "UC Berkeley",
    "UCDAV" : "UC Davis",
    "UCHIC" : "U Chicago",
    "UCI" : "UC Irvine",
    "UCL" : "UCL",
    "UCLA" : "UCLA",
    "UCONN" : "U Connecticut",
    "UCSD" : "UC San Diego",
    "UIUC" : "UIUC",
    "UMICH" : "U Michigan",
    "UMT" : "U Montana",
    "UNC@C" : "UNC-Chapel Hill",
    "VRGN" : "U Virginia",
    "WASH" : "U Washington",
    "WISC" : "U Wisconsin-Madison",
    "WYNE" : "Wayne State U"
}

# Loop through each file to extract information
for file in glob.glob("data/curricula/*.csv"):
    coursecount = -1
    with open(file, "r") as f:
        for line in f:
            coursecount += 1
    name = abbrevdict[file.split("/")[-1].replace(".csv", "")] # Get the university codename
    curfiles.append({"name" : name, "# of courses": coursecount})

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(curfiles) 

# Check if the output file directory exists. If not, make it.
if not os.path.isdir("output/curricula"):
    os.mkdir("output/curricula")

# Output DataFrame to csv
output = os.path.join("output", "curricula", "coursebyuni.csv")

# Output DataFrame to csv
with open(output, "w") as file:
    file.write(pd.DataFrame.to_csv(df, index=False))

"""
Now output the plots we need.
"""

def unique(list1):
    """
    Return unique values from a list list1
    """ 
    unique_list = [] 
    for x in list1: 
        if x not in unique_list: 
            unique_list.append(x) 
    return unique_list

# Sort the names of the universities and number of courses by the number of courses
x = df.sort_values("# of courses")["name"] # x values: names of the universities
y = df.sort_values("# of courses")["# of courses"] # y values: number of courses at each university

# Plot
plt.tight_layout()
plt.bar(x, y) # Plot the data
plt.xticks(x, rotation="vertical") # Add x labels with the names of each university
plt.title("Number of Data Science courses by university") # Title the plot
plt.xlabel("University", rotation="horizontal") # Add the x-label 
plt.ylabel("Number of courses") # Add the y-label
plt.savefig(os.path.join("output", "curricula", "coursebyuni.png"), bbox_inches="tight", pad_inches = 0.0) # Save the plot
