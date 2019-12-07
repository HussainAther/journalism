import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
Analyze poverty data from the Income and Poverty in the United States: 2016
report.
"""

allraces = pd.read_csv("data/food/poverty/allraces.csv")
aa = pd.read_csv("data/food/poverty/asianalone.csv")
aaoic = pd.read_csv("data/food/poverty/asianaloneorincombination.csv")
aapi = pd.read_csv("data/food/poverty/asianandpacificislander.csv")
