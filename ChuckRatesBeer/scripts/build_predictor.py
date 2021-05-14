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
print(X_data_set)
X = asarray(X_data_set)
print(X)
from sklearn import preprocessing
from sklearn import utils

lab_enc = preprocessing.LabelEncoder()
ratings = asarray(df[['rating_score']].copy().values.flatten())
encoded = lab_enc.fit_transform(ratings)
Y = encoded
Y_old = asarray(df[['rating_score']].copy().values.flatten())
from sklearn.linear_model import LogisticRegression


print(X[0])
print(Y_old)
print(Y)

# fit final model
model = LogisticRegression()
model.fit(X, Y)

mapping = dict(zip(range(len(lab_enc.classes_)), lab_enc.classes_))
print(mapping)

from joblib import dump, load
dump(model, 'crb.joblib')

# load('crb.joblib')

# define one new data instance
new_x = asarray([[7.0, 70, 3.97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
new_y = model.predict(new_x)
print(new_y)
print(lab_enc.inverse_transform(new_y))