import json

from sqlalchemy import Column, Integer, Float, Text, String
from sqlalchemy.ext.declarative import declarative_base
import chuck_pyutils.core as utils
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
config = utils.read_config(utils.get_file_path(__file__, "config.ini"))
from sqlalchemy import create_engine

engine = create_engine(config["DATABASE"]["CONNECTION_STR"])


class ChuckRatesBeers(Base):
    __tablename__ = "chuck_rates_beers"
    id = Column(
        "id", Integer, primary_key=True, unique=True, index=True, autoincrement=True
    )
    bid = Column("bid", Integer)
    beer_name = Column("beer_name", String(256))
    brewery_name = Column("brewery_name", String(256))
    chuck_rating = Column("chuck_rating", Float)


# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

with open("../data/chuckratesbeer.json", "r") as data:
    for index, beer in enumerate(json.loads(data.read())):
        crb = ChuckRatesBeers()
        crb.bid = beer["bid"]
        crb.beer_name = beer["beer_name"]
        crb.brewery_name = beer["brewery_name"]
        crb.chuck_rating = float(beer["rating_score"])
        session.add(crb)
    session.commit()
