from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.sampledata.periodic_table import elements
from bokeh.transform import dodge, factor_cmap

output_file("output/criticalminerals/critmincolor.html")

periods = ["I", "II", "III", "IV", "V", "VI", "VII"]
groups = [str(x) for x in range(1, 19)]

df = elements.copy()
df["atomic mass"] = df["atomic mass"].astype(str)
df["group"] = df["group"].astype(str)
df["period"] = [periods[x-1] for x in df.period]
df = df[df.group != "-"]
df = df[df.symbol != "Lr"]
df = df[df.symbol != "Lu"]

# Color map with the crustal abundace (ppm)
# corresponds to a specific color between white and red.
cmap = {"Sb":"#D1C7C7",
       "Ba":"#BAABAB",
       "Be":"#AD1F1F",
       "Li":"#A65959",
       "Nb":"#996666",
       "Ta":"#996666",
       "Sn":"#A65959",
       "Ti":"#854747",
       "Ga":"#FF3333",
       "Co":"#BF4040",
       "Ru":"#C27070",
       "Rh":"#C27070",
       "Pt":"#C27070",
       "Pd":"#C27070",
       "Ir":"#C27070",
       "Os":"#C27070",
       "Mn":"#D1C7C7",
       "F":"#B87A7A",
       "Ge":"#E8E3E3",
       "In":"#E8E3E3",
       "Ce":"#AD8585",
       "Dy":"#AD8585",
       "Er":"#AD8585",
       "Eu":"#AD8585",
       "Gd":"#AD8585",
       "Ho":"#AD8585",
       "La":"#AD8585",
       "Lu":"#AD8585",
       "Nd":"#AD8585",
       "Pr":"#AD8585",
       "Pm":"#AD8585",
       "Sm":"#AD8585",
       "Sc":"#AD8585",
       "Tb":"#AD8585",
       "Tm":"#AD8585",
       "Yb":"#AD8585",
       "Y":"#AD8585",
       "Te":"#7A5252",
       "Re":"#B87A7A",
       "Zr":"#E8E3E3",
       "Hf":"#E8E3E3",
       "V":"#C99C9C"
}

# crustal abundance (ppm)
# with key as atomic number
ca = {
       "51":"34",
       "56":"41",
       "4":"318",
       "3":"118",
       "41":"59",
       "73":"59",
       "50":"113",
       "22":"121",
       "31":"452",
       "27":"212",
       "44":"153",
       "45":"153",
       "78":"153",
       "46":"153",
       "77":"153",
       "76":"153",
       "25":"38",
       "9":"106",
       "32":"23",
       "49":"28",
       "58":"52",
       "66":"52",
       "68":"52",
       "63":"52",
       "64":"52",
       "67":"52",
       "57":"52",
       "71":"52",
       "60":"52",
       "59":"52",
       "61":"52",
       "62":"52",
       "21":"52",
       "65":"52",
       "69":"52",
       "70":"52",
       "39":"52",
       "52":"68",
       "75":"101",
       "40":"27",
       "72":"27",
       "23":"81"
} 
canew = []

dfindex = [0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
             13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
             26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
             39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
             52,  53,  54,  55,  71,  72,  73,  74,  75,  76,  77,  78,  79,
             80,  81,  82,  83,  84,  85,  86,  87, 103, 104, 105, 106, 107,
            108, 109, 110, 111, 112, 113, 114, 115, 116, 117]

for i in dfindex:
    dicti = str(i+1)
    if str(i+1) not in ca:
        canew.append(int(0))
    else:
        canew.append(int(ca[dicti]))

# Add the list of crustal abundances to the 
# DataFrame.
df["ca"] = canew

hovertt = [
    ("Name", "@name"),
    ("Atomic number", "@{atomic number}"),
    ("Atomic mass", "@{atomic mass}"),
    ("Type", "@metal"),
    #("CPK color", "$color[hex, swatch]:CPK"),
    ("Electronic configuration", "@{electronic configuration}"),
    ("Crustal abundance (ppm)", "@ca")
]

p = figure(plot_width=1000, plot_height=450,
           x_range=groups, y_range=list(reversed(periods)),
           tools="hover", toolbar_location=None, tooltips=hovertt)
p.title.text_font_size = "36pt"

r = p.rect("group", "period", 0.95, 0.95, source=df, fill_alpha=0.6,
           color=factor_cmap("symbol", palette=list(cmap.values()), factors=list(cmap.keys())))

text_props = {"source": df, "text_align": "left", "text_baseline": "middle"}

x = dodge("group", -0.4, range=p.x_range)

p.text(x=x, y="period", text="symbol", text_font_style="bold", **text_props)

p.text(x=x, y=dodge("period", 0.3, range=p.y_range), text="atomic number",
       text_font_size="8pt", **text_props)

p.text(x=x, y=dodge("period", -0.35, range=p.y_range), text="name",
       text_font_size="5pt", **text_props)

p.text(x=x, y=dodge("period", -0.2, range=p.y_range), text="atomic mass",
       text_font_size="5pt", **text_props)

p.text(x=["3", "3"], y=["VI", "VII"], text=["LA", "AC"], text_align="center", text_baseline="middle")

p.outline_line_color = None
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_standoff = 0
p.hover.renderers = [r] # only hover element boxes

show(p)
