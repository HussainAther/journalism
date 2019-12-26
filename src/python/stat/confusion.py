# Import the matplotlib.pyplot and numpy libraries.
import matplotlib.pyplot as plt
import numpy as np

# Import the confusion_matrix method from scikit-learn.
from sklearn.metrics import confusion_matrix

"""
Visualize a confusion matrix with labels.
"""

# Tested results from an experiment
y_test = ["cat", "cat", "cat", "cat", "cat", 
          "cat", "cat", "cat", "cat", "cat", 
          "cat", "cat", "cat", "cat", "cat", 
          "cat", "cat", "cat", "cat", "cat"]

# Predicted values
y_pred = ["dog", "cat", "cat", "cat", "cat",
          "cat", "dog", "dog", "cat", "cat", 
          "cat", "cat", "cat", "cat", "cat", 
          "cat", "dog", "dog", "cat", "dog"]

labels = ["cat", "dog"]

# Create the confusion matrix.
cm = confusion_matrix(y_test, y_pred, labels)

# Plot. 
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)

# Label the matrix.
for (i, j), z in np.ndenumerate(cm):
    ax.text(j, i, "{:0.1f}".format(z), ha="center", va="center", fontsize=36, bbox=dict(facecolor="white"))

plt.title("Confusion matrix of the classifier")
fig.colorbar(cax)
ax.set_xticklabels([""] + labels, fontsize="large")
ax.set_yticklabels([""] + labels, fontsize="large")
plt.xlabel("Predicted", fontsize="large")
plt.ylabel("True", fontsize="large")
plt.show()
