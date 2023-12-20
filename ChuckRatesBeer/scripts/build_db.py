import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pprint as pp
import os
from numpy import asarray
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import matplotlib.pyplot as plt
df = pd.read_json("../data/chuckratesbeer.json")
print(df.head())
X_data_set = df[['beer_abv', 'beer_ibu', 'global_rating_score', 'beer_type']].copy()
print(X_data_set)
X_data_set[["Type", "Subtype"]] = X_data_set.beer_type.str.split(" - ", expand=True)
print(X_data_set)
df_type = pd.get_dummies(X_data_set['Type'])
X_data_set = pd.concat([X_data_set, df_type], axis=1)
print(X_data_set)
X_data_set = X_data_set.drop(columns=['beer_type', 'Type', 'Subtype'])








