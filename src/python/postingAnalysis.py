# Tools for data manipulation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import operator
import glob
import os

# Multithreading
from multiprocessing import Pool

# Map plotting tools
from mpl_toolkits.basemap import Basemap 
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon

# Machine learning tools
from sklearn.metrics import auc, classification_report, f1_score, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.svm import SVC

"""
Analysis of Data Science job postings. The position postings were gathered from 5/19/2018 to 5/21/2018, 
keying from major United States cities with populations greater than 250,000. The goal was to evaluate 
these data sets to understand alignment and gaps between industry demand and higher education offerings. 

Usage: "python postanalysis.py"

Use the postings.csv file in the data/posting directory as input files. 
"""
def cross_validation_scores(clf, scoring_function, N=51):
    """
    Used for cross-validating our SVC so it may be generalized to other datasets for an input
    clf (classifier), scoring function (scoring_function), and number of iterations for the
    prediction and cross-validation.
    """
    # Lists for tested, predicted, and corresponding error.
    score = []
    test = []
    predicted = []
    errorlist = []
    for i in range(N):
        # Split the data into training and test data.
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, train_size=.8, random_state=123)
        # Train our model.
        y_score = clf.fit(X_train, y_train).decision_function(X_test)
        # Predict for testing slice.
        y_predicted = clf.predict(X_test)
        # Evaluate performance.
        errors = round(scoring_function(y_test, y_predicted, average="micro"), 2)
        # Add the values to our lists.
        score.append(y_score)
        test.append(y_test)
        predicted.append(y_predicted)
        errorlist.append(float((errors)))
        classreport.append(classification_report(y_test, y_predicted))
    return score, test, predicted, errorlist

def unique(list1):
    """
    Return unique values from a list list1.
    """
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

# Check which directory we are in. If we're not in the main journalism
# directory, then cd to it.
while os.getcwd().split("/")[-1] != "journalism":
    os.chdir("..")

# Check if the output file directory exists. If not, make it.
if not os.path.isdir("output/postings"):
    os.mkdir("output/postings")

# Read the postings.csv as a pandas DataFrame.
df = pd.read_csv("output/postings/extracted.csv")

# Remove the samples for which we don't have data on the city and state.
df = df[df.location != "United States"]

# Initialize list of states and a dictionary of their abbreviations.
states=[]
abbrev = {
    "AK": "Alaska",
    "AL": "Alabama",
    "AR": "Arkansas",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DC": "District of Columbia",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "IA": "Iowa",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "MA": "Massachusetts",
    "MD": "Maryland",
    "ME": "Maine",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MO": "Missouri",
    "MP": "Northern Mariana Islands",
    "MS": "Mississippi",
    "MT": "Montana",
    "NA": "National",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "NE": "Nebraska",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NV": "Nevada",
    "NY": "New York",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VA": "Virginia",
    "VI": "Virgin Islands",
    "VT": "Vermont",
    "WA": "Washington",
    "WI": "Wisconsin",
    "WV": "West Virginia",
    "WY": "Wyoming"
}

abbrev2 = {value: key for key, value in abbrev.items()}

ablist = list(abbrev.keys())

# Make a dictionary of each state's frequency.
statedict = {}

# Get the name of each state for each sample.
for i in list(df["location"]):
    if str(i)[-2:] in abbrev:
        fullname = abbrev[i[-2:]]
        states.append(fullname)
        if fullname in statedict:
            statedict[fullname] += 1
        else:
            statedict[fullname] = 1
    elif i in abbrev2:
        states.append(i)
        if i in statedict:
            statedict[i] += 1
        else:
            statedict[i] = 1

# For states with none.
for i in abbrev2:
    if i not in statedict:
        statedict[i] = 0

# Lambert Conformal map of lower 48 states.
m = Basemap(llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49,
        projection="lcc", lat_1=33, lat_2=45, lon_0=-95)

# Draw state boundaries.
shp_info = m.readshapefile("data/map/st99_d00", "states", drawbounds=True)

# Choose a color for each state based on number of jobs.
colors={}

# Use hot colormap set.
cmap = plt.cm.copper

# Hawaii has 8 main islands but several tiny atolls that extend for many miles.
# This is the area cutoff between the 8 main islands and the tiny atolls.
ATOLL_CUTOFF = 0.005

# Cycle through state names, color each one.
ax = plt.gca()

# List of statenames.
statenames = []

# Keep track of max and min.
maxx = 0
minn =0

# For each state, find a color for it.
for shapedict in m.states_info:
    statename = shapedict["NAME"]
    # Skip Puerto Rico.
    if statename != "Puerto Rico":
        freq = statedict[statename]
        if freq > maxx:
            maxx = freq
        if freq < minn:
            minn = freq
        # Calling colormap with value between 0 and 1 returns
        # rgba value.  Invert color range (hot colors are high
        # population), take sqrt root to spread out colors more.
        colors[statename] = cmap(freq)[:3]
    statenames.append(statename)

# For each state, map and color it.
for nshape, seg in enumerate(m.states):
    # skip DC and Puerto Rico.
    if statenames[nshape] != "Puerto Rico":
    # Offset Alaska and Hawaii to the lower-left corner.
        if statenames[nshape] == "Alaska":  # Scale Alaska appropriately.
            segx = [i[0] for i in seg]
            segy = [i[1] for i in seg]
            lamx = lambda x: .35*float(x) + 1100000
            lamy = lambda y: .35*float(y) - 1300000
            lamxy = lambda x, y: lamx, lamy
            segx = list(map(lamx, segx))
            segy = list(map(lamy, segy))
            seg = np.column_stack((segx, segy))
        elif statenames[nshape] == "Hawaii": # Scale Hawaii appropriately.
            segx = [i[0] for i in seg]
            segy = [i[1] for i in seg]
            lamx = lambda x: float(x) + 5200000
            lamy = lambda y: float(y) - 1400000
            segx = list(map(lamx, segx))
            segy = list(map(lamy, segy))
            seg = np.column_stack((segx, segy))
        color = rgb2hex(colors[statenames[nshape]])
        poly = Polygon(seg, facecolor=color, edgecolor=color)
        ax.add_patch(poly)

print("Max frequency " + str(maxx))
v = np.linspace(minn, maxx)
plt.title("Job density by state")
plt.contourf(colors.values(), 51, cmap="copper")
plt.colorbar(ticks=v)
plt.savefig("output/postings/jobdensity.png")
plt.close()

"""
The rest of this script performs support vector classification, a method of support vector machines,
and fits the data (split between training and testing) to form predictions on the job market.
"""

# Use the education as the training X data and the state as y.
X = []
y = []

# For numerizing the education requirements.
edudict = {
    "B.S.": 1,
    "M.S." : 2,
    "Ph.D.": 3
}

pool = Pool(100)
# For X (known data), we extract the education requirement for the jobs.
# For y (target data), we use the location.
for i in df.index:
    if str(df["location"][i])[-2:] in abbrev:
        if df["education"][i] in edudict:
            X.append(edudict[df["education"][i]])
        else:
            X.append(0)
        y.append(ablist.index(df["location"][i][-2:]))

# Shape into 2D array.
X = np.array(X)
X = X.reshape(-1, 1)

# Learn to predict each class against the other.
# Cross-validate the results.
classreport = []
clf = SVC(kernel="rbf", gamma="scale")
y_score, y_test, y_predicted, errors = cross_validation_scores(clf, f1_score)

# Print out a classification report.
with open("output/postings/classreport.txt", "w") as file:
    for line in classreport:
        file.write(line)

# Plot the Cross-validation error results.
plt.title("Cross-validation Error")
pd.DataFrame(errors).hist(bins=20)
plt.savefig("output/postings/cverror.png")
plt.close()
