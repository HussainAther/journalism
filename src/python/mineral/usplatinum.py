import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
I wish it were Minecraft.
"""

# Read 'em in!
pt = pd.read_csv("data/mineral/csv/Platinum.csv")
usproc = pd.read_csv("data/mineral/csv/USProcessed.csv", index_col="Value")

usproc = usproc.transpose()

pt["Year"] = [int(i) for i in pt["Year"]]
usproc["Year"] = [int(i) for i in usproc.index]

fig = plt.figure()
ax = fig.add_subplot()
plt.plot("Year", "Worldmineproduction", data=pt)
plt.title("World Platinum Production")
plt.ylabel("Thousand Metric Tons")
plt.xlabel("Year")
plt.xticks(range(1990, 2011, 5)) 
plt.savefig("output/mineral/ptworldprod.png")

fig = plt.figure()
ax = fig.add_subplot()
# Palladium Consumption in thousand metric ton
usproc["pgepdcon"] = [float(i)*0.000001 for i in usproc["PlatinumGroupMetals(kg)ConsumptionPalladium"]]
# Platinum Consumption in thousand metric ton
usproc["pgeptcon"] = [float(i)*0.000001 for i in usproc["PlatinumGroupMetals(kg)ConsumptionPlatinum"]]
# Palladium Production in thousand metric ton
usproc["pgeptpro"] = [float(i)*0.000001 for i in usproc["PlatinumGroupMetals(kg)ProductionPalladium"]]
# Platinum Production in thousand metric ton
usproc["pgepdpro"] = [float(i)*0.000001 for i in usproc["PlatinumGroupMetals(kg)ProductionPlatinum"]]
plt.plot("Year", "pgepdcon", data=usproc, label="Palladium Consumption")
plt.plot("Year", "pgeptcon", data=usproc, label="Platinum Consumption")
plt.plot("Year", "pgeptpro", data=usproc, label="Platinum Production")
plt.plot("Year", "pgepdpro", data=usproc, label="Palladium Production")
plt.title("U.S. PGE Production and Consumption")
plt.legend(loc=0)
plt.ylabel("Thousand Metric Tons")
plt.xlabel("Year")
plt.xticks(range(2005, 2010)) 
plt.savefig("output/mineral/pgeusprocon.png")

fig = plt.figure()
ax = fig.add_subplot()
# Iridium, Osmium and Ruthenium Exports 
usproc["irosruexp"] = [float(i)*.000001 for i in usproc["PlatinumGroupMetals(kg)ExportsIridiumosmiumandruthenium"]]
# Palladdium Exports
usproc["pdexp"] = [float(i)*.000001 for i in usproc["PlatinumGroupMetals(kg)ExportsPalladium"]]
# Platinum Exports
usproc["ptexp"] = [float(i)*.000001 for i in usproc["PlatinumGroupMetals(kg)ExportsPlatinum"]]
# Rhodium Exports
usproc["rhexp"] = [float(i)*.00001 for i in usproc["PlatinumGroupMetals(kg)ExportsRhodium"]]
plt.plot("Year", "irosruexp", data=usproc, label="Iridium, Osmium and Ruthenium Exports")
plt.plot("Year", "pdexp", data=usproc, label="Palladium Exports")
plt.plot("Year", "ptexp", data=usproc, label="Platinum Exports")
plt.plot("Year", "rhexp", data=usproc, label="Rhodium Exports")
plt.title("U.S. PGE Exports")
plt.legend(loc=0)
plt.ylabel("Thousand Metric Tons")
plt.xlabel("Year")
plt.xticks(range(2005, 2010)) 
plt.savefig("output/mineral/pgeexp.png")

fig = plt.figure()
ax = fig.add_subplot()
# Iridium Imports
usproc["irimp"] = [float(i)*.00001 for i in usproc["PlatinumGroupMetals(kg)ImportsIridium"]]
usproc["OsmiumImports"] = [float(i) for i in usproc["OsmiumImports"]]
usproc["PalladiumImports"] = [float(i) for i in usproc["PalladiumImports"]]
usproc["PlatinumImports"] = [float(i) for i in usproc["PlatinumImports"]]
usproc["RhodiumImports"] = [float(i) for i in usproc["RhodiumImports"]]
usproc["RutheniumImports"] = [float(i) for i in usproc["RutheniumImports"]]
plt.plot("Year", "irimp", data=usproc, label="Iridium Imports")
plt.plot("Year", "OsmiumImports", data=usproc, label="Osmium Imports")
plt.plot("Year", "PalladiumImports", data=usproc, label="Palladium Imports")
plt.plot("Year", "PlatinumImports", data=usproc, label="Platinum Imports")
plt.plot("Year", "RhodiumImports", data=usproc, label="Rhodium Imports")
plt.plot("Year", "RutheniumImports", data=usproc, color="#000000", label="Ruthenium Imports")
plt.title("U.S. PGE Imports")
plt.legend(loc=0)
plt.ylabel("Thousand Metric Tons")
plt.xlabel("Year")
plt.xticks(range(2005, 2010)) 
plt.savefig("output/mineral/pgeimp.png")
