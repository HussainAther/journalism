import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

"""
Linear regression of salary data.
"""

url = "https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv"
salary = pd.read_csv(url)

y, x = salary.salary, salary.experience
beta, beta0, r_value, p_value, std_err = stats.linregress(x,y)

print("y = %f x + %f , r: %f , r-squared: %f ,\np-value: %f , std_err: %f "
      % (beta, beta0, r_value, r_value**2, p_value, std_err))

print("Regression line with the scatterplot")
yhat = beta * x + beta0 # regression line
plt.plot(x, yhat, "r-", x, y, "o") 
plt.xlabel("Experience (years)") 
plt.ylabel("Salary")
plt.show()
sns.regplot(x="experience", y="salary", data=salary)
