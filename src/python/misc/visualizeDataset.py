import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

"""
Visualize the contents of a dataset using pandas, matplotlib, and seaborn.

Usage: "python visualizeDataset.py"
"""

# Initialize an empty DataFrame.
df = pd.DataFrame()

# Add some random elements to the "x" and "y" columns we create.
df["x"] = random.sample(range(1, 100), 25)
df["y"] = random.sample(range(1, 100), 25)

# Print out the top five elements.
print("top five elements:")

# The .head() function prints out the top five elements of the DataFrame.
print(df.head())

# Display a density plot.
sns.kdeplot(df.y)

# Display a histogram.
plt.hist(df.x, alpha=.3)

# Display a boxplot.
sns.boxplot([df.y, df.x])

# Display a heatmap.
sns.heatmap([df.y, df.x], annot=True, fmt="d")

# Display a cluster map.
sns.clustermap(df)

# Display a scatterplot.
sns.lmplot("x", "y", data=df, fit_reg=False)

# This displays the plots.
plot.show()
