import json

2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
new_dict = {}

with open("../data/chuckratesbeer.json", "r") as data:
    for index, beer in enumerate(json.loads(data.read())):
        new_dict['Day{}'.format(index + 1)] = {'beer_name': beer['beer_name'],
                                               'brewery_name': beer['brewery_name'],
                                               'untappd_url': beer['checkin_url']}
    with open("../data/crb_by_day.json", 'w') as f:
        f.write(json.dumps(new_dict))

class ChuckRatesBeers(BaseModel):
    __tablename__ = "chuck_rates_beers"
    id = db.Column(
        "id", db.Integer, primary_key=True, unique=True, index=True, autoincrement=True
    )
    bid = db.Column("bid", db.Integer,)
    abv = db.Column("abv", db.Integer,)
    ibu = db.Column("ibu", db.Integer,)
    global_rating = db.Column("global_rating", db.Integer, )
    chuck_rating = db.Column("chuck_rating", db.Integer,)