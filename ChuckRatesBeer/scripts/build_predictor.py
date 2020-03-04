import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pprint as pp
import os
from numpy import asarray

df = pd.read_json("../data/chuckratesbeer.json")
# print(df.head())
X_data_set = df[['beer_abv', 'beer_ibu', 'global_rating_score', 'beer_type']].copy()
# print(X_data_set)
X_data_set[["Type", "Subtype"]] = X_data_set.beer_type.str.split(" - ", expand=True)
# print(X_data_set)
df_type = pd.get_dummies(X_data_set['Type'])
print(df_type.columns)
for item in df_type.columns:
    print(item)
X_data_set = pd.concat([X_data_set, df_type], axis=1)
# print(X_data_set)
X_data_set = X_data_set.drop(columns=['beer_type', 'Type', 'Subtype'])
X = asarray(X_data_set)
from sklearn import preprocessing
from sklearn import utils

lab_enc = preprocessing.LabelEncoder()
ratings = asarray(df[['rating_score']].copy().values.flatten())
encoded = lab_enc.fit_transform(ratings)
Y = encoded
Y_old = asarray(df[['rating_score']].copy().values.flatten())
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import LinearSVC


print(X[0])
print(Y_old)
print(Y)
# fit final model
# model = LinearRegression()
model = LogisticRegression()
model.fit(X, Y)
new_x = asarray([[7.0, 70, 3.97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
new_y = model.predict(new_x)
print(new_y)
print(lab_enc.inverse_transform(new_y))
mapping = dict(zip(range(len(lab_enc.classes_)), lab_enc.classes_))
print(mapping)

from joblib import dump, load
dump(model, 'crb.joblib')
#
# load('crb.joblib')
# # define one new data instance
# Xnew = [[-1.07296862, -0.52817175]]
# # make a prediction
# ynew = model.predict(Xnew)
# # show the inputs and predicted outputs
# print("X={}, Predicted={}".format(Xnew[0], ynew[0]))

# bid
# abv
# ibu
# beer_type
# global_rating_score
# rating_score

# from sklearn import svm
# from sklearn import datasets
# clf = svm.SVC(gamma='scale')
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
# print(X)
# print(y)
# clf.fit(X, y)

# Plot outputs
# print(len(X), len(Y))
# plt.scatter(X, Y, color='black')
# # plt.plot(new_x, new_y, color='blue', linewidth=3)
# #
# plt.xticks(())
# plt.yticks(())
#
# plt.show()