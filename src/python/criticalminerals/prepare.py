import geopandas as gpd
import geoplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import shapefile

"""
Create the csv from the critical mineral information
to use as input for the periodic table.
"""

# Use geopandas to read in shapefile as DataFrame. 
gdf = gpd.read_file("data/criticalminerals/PP1802_CritMin_pts.shp")

symbols = {"krypton": "Kr", 
           "copper": "Cu", 
            "rubidium": "Rb", 
            "iodine": "I", "rhenium": "Re", "gold": "Au", "radium": "Ra", "neon": "Ne", "oxygen": "O", "cobalt": "Co", "germanium": "Ge", "titanium": "Ti", "technetium": "Tc", "zinc": "Zn", "astatine": "At", "arsenic": "As", "radon": "Rn", "hydrogen": "H", "fluorine": "F", "polonium": "Po", "platinum": "Pt", "silicon": "Si", "hafnium": "Hf", "meitnerium": "Mt", "lead": "Pb", "sodium": "Na", "thallium": "Tl", "chromium": "Cr", "selenium": "Se", "iridium": "Ir", "seaborgium": "Sg", "ruthenium": "Ru", "tin": "Sn", "actinium": "Ac", "chlorine": "Cl", "osmium": "Os", "sulfur": "S", "tungsten": "W", "lithium": "Li", "hassium": "Hs", "beryllium": "Be", "mercury": "Hg", "yttrium": "Y", "nickel": "Ni", "antimony": "Sb", "barium": "Ba", "potassium": "k", "xenon": "Xe", "bohrium": "Bh", "helium": "He", "dubnium": "Db", "strontium": "Sr", "bromine": "Br", "argon": "Ar", "cadmium": "Cd", "boron": "B", "scandium": "Sc", "carbon": "C", "palladium": "Pd", "silver": "Ag", "vanadium": "V", "phosphorus": "P", "rutherfordium": "Rf", "bismuth": "Bi", "aluminum": "Al", "molybdenum": "Mo", "lanthanum": "La", "nitrogen": "N", "francium": "Fr", "gallium": "Ga", "zirconium": "Zr", "manganese": "Mn", "rhodium": "Ru", "niobium": "Nb", "calcium": "Ca", "tantalum": "Ta", "magnesium": "Mg", "iron": "Fe", "tellurium": "Te", "cesium": "Cs", "indium": "In"}

elem = {}
for i in gdf["CRITICAL_M"]:
    for a in i.lower().replace("and", "").replace(";", "").split(" "):
        if a not in symbols:  
            if a == "barite": 
                if "Ba" not in elem:
                    elem["Ba"] = 1
                else:
                    elem["Ba"] += 1       
            elif a == "fluorite":
                if "F" not in elem:
                    elem["F"] = 1
                else:
                    elem["F"] += 1 
            elif a == "graphie":
                if "C" not in elem:
                    elem["C"] = 1
                else:
                    elem["C"] += 1
            elif a == "platinum-group":
                if "Ru" not in elem:
                    elem["Ru"] = 1
                    elem["Rh"] = 1
                    elem["Pt"] = 1
                    elem["Pd"] = 1
                    elem["Ir"] = 1
                    elem["Os"] = 1
                else:
                    elem["Ru"] += 1
                    elem["Rh"] += 1
                    elem["Pt"] += 1
                    elem["Pd"] += 1
                    elem["Ir"] += 1
                    elem["Os"] += 1
            elif a == "rare-earth":
                if "Ce" not in elem:
                    elem["Ce"] = 1
                    elem["Dy"] = 1
                    elem["Er"] = 1
                    elem["Eu"] = 1
                    elem["Gd"] = 1
                    elem["Ho"] = 1
                    elem["La"] = 1
                    elem["Lu"] = 1
                    elem["Nd"] = 1
                    elem["Pr"] = 1
                    elem["Pm"] = 1
                    elem["Sm"] = 1
                    elem["Sc"] = 1
                    elem["Tb"] = 1
                    elem["Tm"] = 1
                    elem["Yb"] = 1
                    elem["Y"] = 1
                else:
                    elem["Ce"] += 1
                    elem["Dy"] += 1
                    elem["Er"] += 1
                    elem["Eu"] += 1
                    elem["Gd"] += 1
                    elem["Ho"] += 1
                    elem["La"] += 1
                    elem["Lu"] += 1
                    elem["Nd"] += 1
                    elem["Pr"] += 1
                    elem["Pm"] += 1
                    elem["Sm"] += 1
                    elem["Sc"] += 1
                    elem["Tb"] += 1
                    elem["Tm"] += 1
                    elem["Yb"] += 1
                    elem["Y"] += 1
        if a in symbols:
            if symbols[a] not in elem:
                elem[symbols[a]] = 1
            else:
                elem[symbols[a]] += 1

with open("data/criticalminerals/input.csv", "w") as file:
    for i in elem:
        file.write(str(i) + "," + str(elem[i]))
        file.write("\n") 
