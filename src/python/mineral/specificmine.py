import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
au = pd.read_csv("data/mineral/csv/Gold.csv")
fe = pd.read_csv("data/mineral/csv/Iron.csv")
cu = pd.read_csv("data/mineral/csv/Copper.csv")
cu2 = pd.read_csv("data/mineral/csv/Copper2.csv")
cu3 = pd.read_csv("data/mineral/csv/Copper3.csv")
cu4 = pd.read_csv("data/mineral/csv/Copper4.csv")
ta = pd.read_csv("data/mineral/csv/Tantalum.csv")

alldf = [au, fe, cu, cu2, cu3, cu4, ta]

outjson = open("output/mineral/specificall.json", "w")
outhtml = open("output/mineral/specificall.html", "w")

for df in alldf:
    outjson.write(pd.DataFrame.to_json(df, orient="table", index=False))
    outjson.write("\n")
    outhtml.write(pd.DataFrame.to_html(df, index=False))
    outhtml.write("\n")

# range1 = [float(i) for i in cu["Worldmineproduction"].str.replace(",", "").values]
# range2 = [float(i) for i in cu3["Worldrefinedsecondaryproduction"].str.replace(",", "").values]
# range1 = [int(i) for i in range1]
# range2 = [int(i) for i in range2]
# miny = min(range1) 
# maxy = max(range2)

fig = plt.figure()
ax = fig.add_subplot()
cu["Year"] = [int(i) for i in cu["Year"].values]
cu2["Year"] = [int(i) for i in cu2["Year"].values]
cu3["Year"] = [int(i) for i in cu3["Year"].values]
cu4["Year"] = [int(i) for i in cu4["Year"].values]
plt.plot("Year", "Worldmineproduction", data=cu, color="#ffff00", label="Mined Copper")
plt.plot("Year", "Worldrefinedproduction", data=cu2, color="#FFD700", label="Refined Copper")
plt.plot("Year", "Worldrefinedsecondaryproduction", data=cu3, color="#DAA520", label="Secondary Copper")
plt.plot("Year", "Worldrefinedelectrowonproduction", data=cu4, color="#FF8C00", label="Refined Electrowon Copper")
plt.title("World Production of Types of Copper")
plt.legend(loc=0)
plt.xlabel("Year")
plt.ylabel("Thousand metric tons")
plt.xticks(range(1990, 2011, 4))
plt.yticks(range(1000, 18000, 1000))
plt.savefig("output/mineral/copperprod.png")
plt.close()

fig = plt.figure()
ax = fig.add_subplot()
plt.plot("Year", "Worldmineproduction", data=fe, color="b", label="Iron")
plt.plot("Year", "Worldrefinedproduction", data=au, color="y", label="Gold")
plt.plot("Year", "Worldmineproduction", data=ta, color="r", label="Tantalum")
plt.title("World Production of Select Minerals")
plt.legend(loc=0)
plt.xlabel("Year")
plt.ylabel("Thousand metric tons")
plt.yscale("log")
plt.xticks(range(1990, 2011, 4))
# plt.yticks(range(1000, 18000, 1000))
plt.savefig("output/mineral/specificprod.png")
plt.close()
