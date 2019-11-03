# Import numpy for number manipulation
import numpy as np

# Import pandas for data manipulation
import pandas as pd

# Map plotting tools
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize, LogNorm, to_hex
from matplotlib.cm import plasma, inferno, magma, viridis, ScalarMappable

# Bokeh plotting
from bokeh.models import (ColumnDataSource, LinearColorMapper, LogColorMapper, 
	ColorBar, BasicTicker)
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge

"""
Extract information and draw trends from platinum-group elements (PGE)
with nickel and chromium mineralization.
"""

# Read the .txt file as a pandas DataFrame df
df = pd.read_csv("data/nicr/nicrpge.txt", sep="|", encoding = "ISO-8859-1")

elementlist = [
 "Ac",
 "Ag",
 "Al",
 "Am",
 "Ar",
 "As",
 "At",
 "Au",
 "B",
 "Ba",
 "Be",
 "Bh",
 "Bi",
 "Bk",
 "Br",
 "C",
 "Ca",
 "Cd",
 "Ce",
 "Cf",
 "Cl",
 "Cm",
 "Cn",
 "Co",
 "Cr",
 "Cs",
 "Cu",
 "Db",
 "Ds",
 "Dy",
 "Er",
 "Es",
 "Eu",
 "F", 
 "Fe",
 "Fl",
 "Fm",
 "Fr",
 "Ga",
 "Gd",
 "Ge",
 "H", 
 "He",
 "Hf",
 "Hg",
 "Hs",
 "I", 
 "In",
 "Ir",
 "K",
 "Kr",
 "La",
 "Li",
 "Lr",
 "Lu",
 "Lv",
 "Mc",
 "Md",
 "Mg",
 "Mn",
 "Mo",
 "Mt",
 "N",
 "Na",
 "Nb",
 "Nd",
 "Ne",
 "Nh",
 "Ni",
 "No",
 "Np",
 "O",
 "Og",
 "Os",
 "P", 
 "Pa",
 "Pb",
 "Pd",
 "Pm",
 "Po",
 "Pr",
 "Pt",
 "Pu",
 "Ra",
 "Rb",
 "Re",
 "Rf",
 "Rg",
 "Rh",
 "Rn",
 "Ru",
 "S", 
 "Sb",
 "Sc",
 "Se",
 "Sg",
 "Si",
 "Sm",
 "Sn",
 "Sr",
 "Ta",
 "Tb",
 "Tc",
 "Te",
 "Th",
 "Ti",
 "Tl",
 "Tm",
 "Ts",
 "U", 
 "V", 
 "W", 
 "X",
 "Y", 
 "Yb",
 "Zn",
 "Zr"]

# Frequency of each element dictionary
elementfreq = {
 "Ac": 0,
 "Ag": 0,
 "Al": 0,
 "Am": 0,
 "Ar": 0,
 "As": 0,
 "At": 0,
 "Au": 0,
 "B": 0,
 "Ba": 0,
 "Be": 0,
 "Bh": 0,
 "Bi": 0,
 "Bk": 0,
 "Br": 0,
 "C": 0,
 "Ca": 0,
 "Cd": 0,
 "Ce": 0,
 "Cf": 0,
 "Cl": 0,
 "Cm": 0,
 "Cn": 0,
 "Co": 0,
 "Cr": 0,
 "Cs": 0,
 "Cu": 0,
 "Db": 0,
 "Ds": 0,
 "Dy": 0,
 "Er": 0,
 "Es": 0,
 "Eu": 0,
 "F": 0,
 "Fe": 0,
 "Fl": 0,
 "Fm": 0,
 "Fr": 0,
 "Ga": 0,
 "Gd": 0,
 "Ge": 0,
 "H": 0,
 "He": 0,
 "Hf": 0,
 "Hg": 0,
 "Hs": 0,
 "I": 0,
 "In": 0,
 "Ir": 0,
 "K": 0,
 "Kr": 0,
 "La": 0,
 "Li": 0,
 "Lr": 0,
 "Lu": 0,
 "Lv": 0,
 "Mc": 0,
 "Md": 0,
 "Mg": 0,
 "Mn": 0,
 "Mo": 0,
 "Mt": 0,
 "N": 0,
 "Na": 0,
 "Nb": 0,
 "Nd": 0,
 "Ne": 0,
 "Nh": 0,
 "Ni": 0,
 "No": 0,
 "Np": 0,
 "O": 0,
 "Og": 0,
 "Os": 0,
 "P": 0,
 "Pa": 0,
 "Pb": 0,
 "Pd": 0,
 "Pm": 0,
 "Po": 0,
 "Pr": 0,
 "Pt": 0,
 "Pu": 0,
 "Ra": 0,
 "Rb": 0,
 "Re": 0,
 "Rf": 0,
 "Rg": 0,
 "Rh": 0,
 "Rn": 0,
 "Ru": 0,
 "S": 0,
 "Sb": 0,
 "Sc": 0,
 "Se": 0,
 "Sg": 0,
 "Si": 0,
 "Sm": 0,
 "Sn": 0,
 "Sr": 0,
 "Ta": 0,
 "Tb": 0,
 "Tc": 0,
 "Te": 0,
 "Th": 0,
 "Ti": 0,
 "Tl": 0,
 "Tm": 0,
 "Ts": 0,
 "U": 0,
 "V": 0,
 "W": 0,
 "X": 0,
 "Y": 0,
 "Yb": 0,
 "Zn": 0,
 "Zr": 0
}

# PGE counter
PGE = 0

# Extract the number of elements to use as the frequency.
for index, row in df.iterrows():
    for elem in row["Commod_gp"].replace(" ","").split(","):
        if elem in elementfreq:
            elementfreq[elem] += 1
        elif elem == "PGE":
            PGE += 1

data_elements = list(elementfreq) 
data_elements.append("PGE")
data = elementfreq.values()
data.append(PGE)

# Colormap settings
cmap = plasma
bokeh_palette = "Plasma256"

# Define number of and groups.
period_label = ['1', '2', '3', '4', '5', '6', '7']
group_range = [str(x) for x in range(1, 19)]

# Define matplotlib and bokeh color map.
color_mapper = LinearColorMapper(palette = bokeh_palette, low=min(data), 
		high=max(data))
norm = Normalize(vmin = min(data), vmax = max(data))
color_scale = ScalarMappable(norm=norm, cmap=cmap).to_rgba(data,alpha=None)

# Color specs
blank_color = "#c4c4c4"
color_list = []
for i in range(len(elements)):
    color_list.append(blank_color)

# Other specs
width = 1050
alpha = 0.65
cbar_standoff = 12
cbar_fontsize = 12
cbar_height = 1000

# Compare elements in dataset with elements in periodic table.
for i, data_element in enumerate(data_elements):
    element_entry = elements.symbol[elements.symbol.str.lower() == data_element.lower()]
    color_list[i] = to_hex(color_scale[i])

# Define figure properties for visualizing data.
source = ColumnDataSource(
    data=dict(
        group=[str(x) for x in elements["group"]],
        period=[str(y) for y in elements["period"]],
        sym=elements["symbol"],
        atomic_number=elements["atomic number"],
        type_color=color_list
    )
)

# Plot the periodic table.
p = figure(x_range=group_range, y_range=list(reversed(period_label)), tools="save")
p.plot_width = width
p.outline_line_color = None
p.toolbar_location = "above"
p.rect("group", "period", 0.9, 0.9, source=source,
       alpha=alpha, color="type_color")
p.axis.visible = False
text_props = {
    "source": source,
    "angle": 0,
    "color": "black",
    "text_align": "left",
    "text_baseline": "middle"
}
x = dodge("group", -0.4, range=p.x_range)
y = dodge("period", 0.3, range=p.y_range)
p.text(x=x, y="period", text="sym",
       text_font_style="bold", text_font_size="16pt", **text_props)
p.text(x=x, y=y, text="atomic_number",
       text_font_size="11pt", **text_props)

color_bar = ColorBar(color_mapper=color_mapper,
	ticker=BasicTicker(desired_num_ticks=10),border_line_color=None,
	label_standoff=cbar_standoff,location=(0,0),orientation="vertical",
    scale_alpha=alpha,major_label_text_font_size=str(cbar_fontsize)+"pt")

if cbar_height is not None:
	color_bar.height = cbar_height

p.add_layout(color_bar,"right")
p.grid.grid_line_color = None
show(p)
