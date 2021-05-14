# from sklearn import datasets
# from sklearn.preprocessing import StandardScaler
# from sklearn.cluster import MeanShift
# import matplotlib.pyplot as plt
# from itertools import cycle
# import numpy as np
#
# iris = datasets.load_iris()
# features = iris.data
#
# scaler = StandardScaler()
# features_std = scaler.fit_transform(features)
#
# cluster = MeanShift(n_jobs=-1)
# # print(cluster.labels_)
#
# model = cluster.fit(features_std)
# print(model.labels_)
# print(model.cluster_centers_)
#
# labels = model.labels_
# cluster_centers = model.cluster_centers_
#
# labels_unique = np.unique(labels)
# n_clusters_ = len(labels_unique)
#
# colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
# for k, col in zip(range(n_clusters_), colors):
#     my_members = labels == k
#     cluster_center = cluster_centers[k]
#     plt.plot(features[my_members, 0], features[my_members, 1], col + '.')
#     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=14)
# plt.title('Estimated number of clusters: %d' % n_clusters_)
# plt.show()

# plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')
#
# import numpy as np
# from sklearn.cluster import MeanShift, estimate_bandwidth
# from sklearn.datasets import make_blobs
#
# # #############################################################################
# # Generate sample data
# centers = [[1, 1], [-1, -1], [1, -1]]
# X, _ = make_blobs(n_samples=10000, centers=centers, cluster_std=0.6)
#
# # #############################################################################
# # Compute clustering with MeanShift
#
# # The following bandwidth can be automatically detected using
# bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
#
# ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
# ms.fit(X)
# labels = ms.labels_
# cluster_centers = ms.cluster_centers_
#
# labels_unique = np.unique(labels)
# n_clusters_ = len(labels_unique)
#
# print("number of estimated clusters : %d" % n_clusters_)
#
# # #############################################################################
# # Plot result
# import matplotlib.pyplot as plt
# from itertools import cycle
#
# plt.figure(1)
# plt.clf()
#
# colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
# for k, col in zip(range(n_clusters_), colors):
#     my_members = labels == k
#     cluster_center = cluster_centers[k]
#     plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
#     plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
#              markeredgecolor='k', markersize=14)
# plt.title('Estimated number of clusters: %d' % n_clusters_)
# plt.show()

# import numpy as np
# from sklearn.cluster import KMeans
# from sklearn import datasets
#
# np.random.seed(0)
#
# # Use Iris data
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
# print(X)
# print(y)
# # KMeans with 3 clusters
# clf =  KMeans(n_clusters=3)
# clf.fit(X,y)
#
# #Coordinates of cluster centers with shape [n_clusters, n_features]
# clf.cluster_centers_
# #Labels of each point
# clf.labels_
#
# # Nice Pythonic way to get the indices of the points for each corresponding cluster
# mydict = {i: np.where(clf.labels_ == i)[0] for i in range(clf.n_clusters)}
#
# # Transform this dictionary into list (if you need a list as result)
# dictlist = []
# for key, value in mydict.items():
#     temp = [key,value]
#     dictlist.append(temp)
# print(dictlist)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np

# do chuck work
iris = datasets.load_iris()
features = iris.data
print(features)
scaler = StandardScaler()
features_std = scaler.fit_transform(features)
print(features_std)

cluster = KMeans(n_clusters=3, random_state=0, n_jobs=-1)

model = cluster.fit(features_std)
print(model.labels_)
print(model.cluster_centers_)

# Nice Pythonic way to get the indices of the points for each corresponding cluster
mydict = {i: np.where(model.labels_ == i)[0] for i in range(model.n_clusters)}

# Transform this dictionary into list (if you need a list as result)
dictlist = []
for key, value in mydict.items():
    temp = [key,value]
    dictlist.append(temp)
print(dictlist)

