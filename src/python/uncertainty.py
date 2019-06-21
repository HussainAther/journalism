import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import ttest_ind, ttest_1samp, poisson

"""
Simple statistics and methods to quantify uncertainty
"""

# Make up some data I don't know
# N = 25
N = 75
mu1 = 7
mu2 = 10
sd = 5

# Generate random data.
data1 = sd * np.random.randn(N) + mu1
data2 = sd * np.random.randn(N) + mu2

# Histograms
fig, ax = plt.subplots()
ax.hist(data1)
ax.hist(data2)

result = ttest_ind(data1, data2)
print(result.pvalue)

# Means and standard deviations of each dataset
mn1 = np.mean(data1)
mn2 = np.mean(data2)

std1 = np.std(data1)
std2 = np.std(data2)

# Now standard error
ste1 = std1 / np.sqrt(N)
ste2 = std2 / np.sqrt(N)

fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
for ax, err1, err2, nm in zip(axs, [std1, ste1], [std2, ste2], ["std", "ste"]):
    ax.vlines([0, 1], [mn1 - err1, mn2 - err2], [mn1 + err1, mn2 + err2])
    _ = plt.setp(ax, xlim=[-1, 2], title='Error: {}'.format(nm))
plt.tight_layout()

# Show histograms with standard error
fig, ax = plt.subplots()
ax.hist(data1)
ax.hist(data2)

ymax = ax.get_ylim()[-1]
for ii, (imn, iste, c) in enumerate([(mn1, ste1, "b"), (mn2, ste2, "g")]):
    ax.hlines(ymax + 1 + ii, imn - iste, imn + iste, lw=6, color=c)
ax.set_ylim([None, ax.get_ylim()[-1] + 2])

# Calculate uncertainty
data = np.random.poisson(lam=2, size=5000)

mn = data.mean()
ste = data.std() / np.sqrt(data.shape[0])

fig, ax = plt.subplots()
ax.hist(data, bins=np.arange(0, 10, 1))
ax.hlines(ax.get_ylim()[-1] + 10, mn - ste, mn + ste, lw=10)

# Bootstrap: Randomly sample data, calculate mean, repeat and calculate percentiles of the distribution
n_boots = 1000
means = np.zeros(n_boots)
for ii in range(n_boots):
    ixs_sample = np.random.randint(0, data.shape[0], size=data.shape[0])
    sample = data[ixs_sample]
    means[ii] = sample.mean()

# Calculate confidence intervals.
clo, chi = np.percentile(means, [2.5, 97.5])
fig, ax = plt.subplots()
ax.hist(means, histtype="step", color="r")
ax.hlines(ax.get_ylim()[-1] + 10, clo, chi, lw=10, color="r")
ax.hlines(ax.get_ylim()[-1] + 20, mn - ste, mn + ste, lw=10, color="g")
