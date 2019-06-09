# import requests
# import json
#
# with open("../data/chuckratesbeer.json", "r") as data:
#     for index, beer in enumerate(json.loads(data.read())):
#         print(index, beer)
#         r = requests.get(beer.get("photo_url"))
#
#         if r.status_code == 200:
#             with open("../data/pics_raw/Day{}.jpg".format(index+1), 'wb') as f:
#                 f.write(r.content)

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pprint as pp
import os

df = pd.read_json("../data/chuckratesbeer.json")
print(df.head())
new = df[['bid', 'beer_abv', 'beer_ibu', 'beer_name', 'beer_type', 'brewery_city', 'brewery_country', 'global_rating_score', 'serving_type', 'rating_score']].copy()
print(new.head())

# dists = cosine_similarity(new)
#
# # stuff the distance matrix into a dataframe so it's easier to operate on
# dists = pd.DataFrame(dists, columns=new.index)
#
#
#
# print(dists.head())


from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
# generate regression dataset
X, y =
print(X)
print(y)
# fit final model
model = LinearRegression()
model.fit(X, y)
from joblib import dump, load
dump(model, 'filename.joblib')

load('filename.joblib')
# define one new data instance
Xnew = [[-1.07296862, -0.52817175]]
# make a prediction
ynew = model.predict(Xnew)
# show the inputs and predicted outputs
print("X=%s, Predicted=%s" % (Xnew[0], ynew[0]))
# bid
# abv
# ibu
# beer_name
# beer_type
# brewery_city
# brewery_country
# global_rating_score
# serving_type
# rating_score