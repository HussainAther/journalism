import re
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import subprocess

from datetime import datetime

"""
Extract info from each raw input file.

Usage: "python extractInfo.py"
"""

# Start the timer.
startTime = datetime.now()

def getSalary(s):
    """
    For some string s, return the salary by finding only the numbers in the string that 
    are of five digits or more. We aren't going to use this function. The raw input data
    is such that there isn't a clear-cut "salary" string in the text. This function will, 
    instead in some cases, find phone numbers or zip codes.
    """
    salary = 0
    for i in re.findall(r"[-+]?\d*\.\d+|\d+", s): # For each numerical sequence in the string,
        if float(i) > 9999 and float(i) > salary: # if it is greater than the current salary and it is a viable salary,
            salary = i # save it.
    if salary != 0: # If we have found a salary,
        return salary # return the salary.
    return None # If not, then return None.

def edu(s):
    """
    Text the string s for educational requirements (Ph.D., M.S., B.S.). 
    Return a string containing the educational requirements.
    """
    req = [] # List of requirements.
    if "PhD" in s or "Ph.D." in s or "Ph. D." in s or "Any Graduate" in s:
        req.append("Ph.D.")
    elif "MS" in s or "M.S." in s or "M.Sc" in s or "M.Sc" in s or "Master" in s or "Any Graduate" in s:
        req.append("M.S.")
    elif "BS" in s or "B.S." in s or "B.Sc." in s or "Bachelor" in s or "B.Tech" in s:
        req.append("B.S.") 
    return req # Return the list of educational requirements in this string.

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while os.getcwd().split("/")[-1] != "journalism":
    os.chdir("..")

# Read the csv as a pandas DataFrame.
df = pd.read_csv("data/postings/postings.csv")

# Initialize a list that will contain each educational requirement.
edulist = []

# Loop through the DataFrame to extract information.
for index, row in df.T.iteritems():
    currEdu = [] # Initialize educational requirements.
    currEdu = edu(str(row["description"]))
    currEdu = " ".join(str(i) for i in currEdu)
    edulist.append(currEdu)

# Add the educational requirements to the DataFrame.
df["education"] = edulist

# Check if the output file directory exists. If not, make it.
if not os.path.isdir("output/postings"):
    os.mkdir("output/postings")

# Output DataFrame to csv.
output = os.path.join("output", "postings", "extracted.csv")
with open(output, "w") as file:
    file.write(pd.DataFrame.to_csv(df))

# Count the number of programs per degree requirement.
nonenum = len(df[df.education == ""].index) # No education requirement was found.
bsnum = len(df[df.education == "B.S."].index)
msnum = len(df[df.education == "M.S."].index)
phdnum = len(df[df.education == "Ph.D."].index)
labels = ["none", "B.S.", "M.S.", "Ph.D"]

# Print the output.
print("Number of jobs with no educational requirements: " + str(nonenum))
print("Number of jobs with a B.S. requirement: " + str(bsnum))
print("Number of jobs with an M.S. requirement: " + str(msnum))
print("Number of jobs with a Ph.D. requirement: " + str(phdnum))

# Plot the data.
plt.bar(labels, [nonenum, bsnum, msnum, phdnum])
# Title the plot
plt.title("Educational requirements for data science positions")
# Add the x-label
plt.xlabel("Degree requirements", rotation="horizontal")
# Add the y-label
plt.ylabel("Number of positions")
# Save the plot
plt.savefig(os.path.join("output", "postings", "edureq.png"))

# Print how long this script took to run.
print("Total run time : " + str(datetime.now() - startTime))
