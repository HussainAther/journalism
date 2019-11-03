import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
cu = pd.read_csv("data/mineral/csv/Copper.csv")
cu2 = pd.read_csv("data/mineral/csv/Copper2.csv")
cu3 = pd.read_csv("data/mineral/csv/Copper3.csv")
cu4 = pd.read_csv("data/mineral/csv/Copper4.csv")
usmine = pd.read_csv("data/mineral/csv/USMined.csv", index_col="Value")
usproc = pd.read_csv("data/mineral/csv/USProcessed.csv", index_col="Value")

alldf = [cu, cu2, cu3, cu4]

usmine = usmine.transpose()
usproc = usproc.transpose()

cu["Year"] = [int(i) for i in cu["Year"]]
cu2["Year"] = [int(i) for i in cu2["Year"]]
cu3["Year"] = [int(i) for i in cu3["Year"]]
cu4["Year"] = [int(i) for i in cu4["Year"]]
usmine["Year"] = [int(i) for i in usmine.index]
usproc["Year"] = [int(i) for i in usproc.index]

outjson = open("output/mineral/uscopper.json", "w")
outhtml = open("output/mineral/uscopper.html", "w")

for df in alldf:
    outjson.write(pd.DataFrame.to_json(df, orient="table", index=False))
    outjson.write("\n")
    outhtml.write(pd.DataFrame.to_html(df, index=False))
    outhtml.write("\n")

fig = plt.figure()
ax = fig.add_subplot()
plt.plot("Year", "U.S.mineproduction", data=cu, color="#ffff00", label="Mined Copper")
plt.plot("Year", "U.S.refinedproduction", data=cu2, color="#FFD700", label="Refined Copper")
plt.plot("Year", "U.S.refinedsecondaryproduction", data=cu3, color="#DAA520", label="Secondary Copper")
plt.plot("Year", "U.S.refinedelectrowonproduction", data=cu4, color="#FF8C00", label="Refined Electrowon Copper")
plt.title("U.S. Production of Types of Copper")
plt.legend(loc=0)
plt.xlabel("Year")
plt.ylabel("Thousand metric tons")
plt.yscale("log")
plt.xticks(range(1990, 2011, 4))
plt.savefig("output/mineral/uscopperprod.png")

fig = plt.figure()
ax = fig.add_subplot()
# Copper Consumption Reported in Thousand Metric Tons 
usproc["cuconretmt"] = [float(i)/1000 for i in usproc["Copper(mt)ConsumptionReported"]] 
# Copper Consumption Apparent in Thousand Metric Tons 
usproc["cuconappmt"] = [float(i)/1000 for i in usproc["Copper(mt)ConsumptionApparent"]]
plt.plot("Year", "cuconretmt", data=usproc, color="b", label="U.S. Reported Processed Copper Consumption")
plt.plot("Year", "cuconappmt", data=usproc, color="m", label="U.S. Apparent Processed Copper Consumption")
plt.title("U.S. Processed Copper Consumption")
plt.ylabel("Thousand metric tons")
plt.xlabel("Year")
plt.xticks(range(2005, 2010))
plt.legend(loc=0)
plt.savefig("output/mineral/usproccoppercon.png")

fig = plt.figure()
ax = fig.add_subplot()
# Total Copper Production in Thousand Metric Tons 
usproc["totcuprodtmt"] = [float(i)/1000 for i in usproc["Copper(mt)Production"]] 
# Smelter Production in Thousand Metric Tons 
usproc["smecuprodtmt"] = [float(i)/1000 for i in usproc["Copper(mt)Smelter"]] 
# Refined Production in Thousand Metric Tons 
usproc["refcuprodtmt"] = [float(i)/1000 for i in usproc["Copper(mt)Refinery"]]
# Secondary Production in Thousand Metric Tons 
usproc["seccuprodtmt"] = [float(i)/1000 for i in usproc["Copper(mt)Secondary"]]
# Copper-Sulfate Production in Thousand Metric tons
usproc["csprodtmt"] = [float(i)/1000 for i in usproc["Copper(mt)Copper-Sulfate"]] 
plt.plot("Year", "totcuprodtmt", data=usproc, color="#000000", label="U.S. Total Copper Production")
plt.plot("Year", "smecuprodtmt", data=usproc, color="r", label="U.S. Smelted Copper Production")
plt.plot("Year", "refcuprodtmt", data=usproc, color="g", label="U.S. Refined Copper Production")
plt.plot("Year", "seccuprodtmt", data=usproc, color="y", label="U.S. Secondary Copper Production")
plt.plot("Year", "csprodtmt", data=usproc, color="b", label="U.S. Copper-Sulfate Production")
plt.title("U.S. Copper Production")
plt.ylabel("Thousand metric tons")
plt.xlabel("Year")
plt.xticks(range(2005, 2010))
plt.legend(loc=0)
plt.savefig("output/mineral/usproccopperprod.png")
