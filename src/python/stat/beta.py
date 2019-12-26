# Import `numpy` as `np` for ease of use.
import numpy as np

# Import `matplotlib` as `plt` for plotting, and
# import `stats` from `scipy` for the Bernoulli distribution.
from matplotlib import pyplot as plt
from scipy import stats

"""
Plot Bernoulli (beta) distributions of six coin flipping tests.
"""

# Number of coins flipped in each test
t = [0, 2, 10, 20, 50, 500] 

# Draw from the Bernoulli distribution
# in generating probability of flipping heads
# for the case of 500 coin flips. The ".5" indicates
# the probability of flipping heads. The "t[-1]" tells 
# you that we're using the final value of the "t" array.
data = stats.bernoulli.rvs(0.5, size=t[-1])
    
# Get the numbers for the x-axis.
x = np.linspace(0, 1, 100)

# The `enumerate()` function lets you loop through a list
# with two variables: one for the index of the list value (i)
# and the other for the list value (N).

# Loop through each number of trials and add more
# coin toss data based on how many heads are flipped.
for i, N in enumerate(t):
    # Get the number of heads from the random samples
    # of the Bernoulli distribution.
    heads = data[:N].sum()

    # Plot.
    # Set the `ax` variable as the subplot with
    # three rows and two columns.
    ax = plt.subplot(len(t)/2, 2, i+1)
    
    # Set the title of each plot.
    ax.set_title("%s trials, %s heads" % (N, heads))
   
    # Set the x- and y-axis labels.
    plt.xlabel("$P(H)$, Probability of Heads")
    plt.ylabel("Density")

    # Plot the y-axis range. We only need to do this
    # once so we do it on i == 0.
    if i == 0:
        plt.ylim([0.0, 2.0])
    
    # Don't show y-axis tick marks.
    plt.setp(ax.get_yticklabels(), visible=False)
                
    # Create and plot a  Beta distribution to represent the 
    # posterior belief in fairness of the coin.
    y = stats.beta.pdf(x, 1 + heads, 1 + N - heads)

    # Plot everything with the tosses and heads counts.
    plt.plot(x, y, label="observe %d tosses,\n %d heads" % (N, heads))

    # Fill each line plot under the curve. 
    plt.fill_between(x, 0, y, color="#aaaadd", alpha=0.5)

    # Expand plot to cover full width/height and show it.
    plt.tight_layout()
    plt.show()
