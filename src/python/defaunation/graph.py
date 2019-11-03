import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Defaunation graphs
"""

df = pd.DataFrame.from_csv("data/defaunation/gardneretal.csv", encoding="windows-1252")

# plt.figure(figsize=(4,23))
plt.figure()
df["Region"].value_counts().plot.bar(stacked=True)
plt.title("Defaunation papers across regions")
plt.xlabel("Region")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/defaunation/region.png") 

# plt.figure(figsize=(10,4))
plt.figure()
df["Study design"].value_counts().plot.barh(stacked=True)
plt.title("Defaunation papers by study design")
plt.ylabel("Study design")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("output/defaunation/studydesign.png")

plt.figure()
df["Fauna"].value_counts().plot.barh(stacked=True)
plt.title("Defaunation papers by fauna")
plt.ylabel("Fauna")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("output/defaunation/fauna.png")

plt.figure()
df["Vegetation response"].value_counts().plot.barh(stacked=True)
plt.title("Defaunation papers by vegetation response")
plt.ylabel("Vegetation response")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("output/defaunation/vegetation.png")

plt.figure()
df["Interaction"].value_counts().plot.barh(stacked=True)
plt.title("Defaunation papers by interaction")
plt.ylabel("Animal-Plant Interaction")
plt.xlabel("Count")
plt.tight_layout()
plt.savefig("output/defaunation/interaction.png")
