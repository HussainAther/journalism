import re
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

"""
This script converts a list of citations into a readable .csv with a pandas
DataFrame as a middle product.
Usage: "python citetocsv.py citations"
For example: "python src/python/citetocsv.py data/citation/statllcpub.txt"
Input files must end with a suffix (such as .txt) and follow
Scientific Style and Format for Authors, Editors, and Publishers.
Comments in the input files must be in lines beginning with #.
"""

# Initialize list of sets
listo = []
labels = ["authors", "title", "published", "year"] 

# Read the input filename from the commandline argument
input = sys.argv[1]
name = input.split("/")[-1][:-3]

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while os.getcwd().split("/")[-1] != "journalism":
    os.chdir("..")

# Read input file of publications and create list of
# sets with their information
with open(input, "r") as file:
    for line in file:
        if not line.startswith("#"): # Ignore commented lines
            authors = ''.join(line.split('"')[0].split(',')).replace(' and', '').replace("\n", "") # Extract the list of authors
            if line.count('"') == 2: # if there are no quotes in the actual title of the manuscript 
                title = line.split('"')[1].replace("\n", "") # Extract the title
            else: # if there are quotes in the actual title of the manuscript
                title = '"'.join(line.split('"')[1:4]).replace("\n", "") # Extract the title 
            afterfinalquote = ''.join(line.split('"')[-1]).replace("\n", "") # Extract the text following the final quote
            if len(afterfinalquote.split(',')) == 3: # if we have three fields following the final quotation mark
                published = afterfinalquote.split(',')[0].replace("\n", "") # Extract the publication information
            else: # if we have four fields following the final quotation mark 
                published = ', '.join(afterfinalquote.split(',')[:2] + [afterfinalquote.split(',')[-1]]).replace("\n", "") # Extract the publication information
            year = str(int(re.match(r'.*([1-3][0-9]{3})', line).group(1))) # Extract the year
            listo.append((authors, title, published, year)) # Append to our list of sets
 
# Convert list of sets to DataFrame                
df = pd.DataFrame.from_records(listo, columns=labels)

# Check if the output file directory exists. If not, make it.
if not os.path.isdir("output/citation"):
    os.mkdir("output/citation")

# Create the output file
output = os.path.join("output/", "citation", str(name) + "csv")

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

x = sorted(unique(list(df["year"]))) # x values: the years
y = [] # y values: the number of publications in that year
for year in x:
    y.append(len(df.loc[df["year"] == year]))

# Plot
plt.bar(x, y) # Plot the data
plt.title(str(name) + "by year") # Title the plot
plt.xlabel("Years") # Add the x label
plt.ylabel("Publications") # Add the y label
plt.savefig(os.path.join("output/", "citation", str(name) + "year.png")) # Save the plot
