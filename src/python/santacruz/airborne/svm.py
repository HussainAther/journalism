import itertools
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.svm import SVC 
from sklearn.metrics import classification_report,confusion_matrix
plt.style.use("seaborn-poster")

"""
Support vector machine (SVM svm).
"""

# Read in data.
raddf = pd.read_csv("data/santacruz/airborne/santa_cruz_rad.csv", index_col="fid", encoding="utf-8")
magdf = pd.read_csv("data/santacruz/airborne/santa_cruz_mag.csv", index_col="fid", encoding="utf-8")

# Extract data of interest for the svm.
y = [] # The target values of interest with a specific number assocaited with each target
ynames = [] # Names for each target value
count = 0 # Used for keeping track of each target
for i in range(len(magdf["geology"])):
    if i in ynames:
        y.append(ynames.index(i))
    else:
        count += 1
        y.append(count)
        ynames.append(count)
X = [list(a) for a in zip(magdf["latitude"], magdf["longitude"])] # Features we test
target = ynames
feature = ["latitude", "longitude"] # Feature names

# Let's get machine learning in this joint. 
clf = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape=None, degree=3, gamma="auto", kernel="rbf",
    max_iter=100, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)

# Fit.
clf.fit(X,y)

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title="Confusion matrix",
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    fig = plt.figure(figsize=(10, 8)) 
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.savefig("output/santacruz/airborne/confusion.png")
    plt.close()
    
# Plotting decision regions
def plot_desicion_boundary(X, y, clf, title = None):
    """
    Helper function to plot the decision boundary for the SVM
    """
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure(figsize = (10, 8))
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, alpha=0.8)
    if title is not None:
        plt.title(title)
    # highlight the support vectors
    #plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80,
    #            facecolors="none", zorder=10)
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.savefig("output/santacruz/airborne/decisionboundary.png")
    plt.close()

# # Look at the data.
# plt.figure(figsize = (10,8))
# for i, c, s in (zip(range(3), ["b", "g", "r"], ["o", "^", "*"])):
#     ix = y == i
#     plt.scatter(X[:, 0][ix], X[:, 1][ix], color = c, marker = s, s = 60, label = target[i])
# 
# plt.legend(loc = 2, scatterpoints = 1)
# plt.xlabel("Latitude - " + feature[0])
# plt.ylabel("Longitude - " + feature[1])
# plt.savefig("output/santacruz/airborne/plot.png")

# Predict results from the test data.
predicted = clf.predict(X)

# # Plot the confusion matrix.
# cm = confusion_matrix(y,predicted)
# plot_confusion_matrix(cm, classes=target,
#                       title="Confusion matrix, without normalization")

# # Plot the decision boundary.
# plot_desicion_boundary(X, y, clf)
