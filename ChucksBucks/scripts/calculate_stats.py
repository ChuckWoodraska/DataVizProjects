# # total distance
# # longest single point to point
# # longest total single buck
# # total entries
# # SELECT COUNT(*) FROM buck_entries;
# # 487
# # total unique dollars checked in (do percentage since you didnt check all them in yourself)
# # SELECT COUNT(DISTINCT fk_serial_number) FROM buck_entries;
# # 318/365 = 87.12%
# # largest number of check ins
# # SELECT COUNT(*), fk_serial_number FROM buck_entries GROUP BY fk_serial_number;
# # 5,A52233859C
# # 5,C87665168C
# # 5,E72974408A
# # 5,J41218200C
#
# # Super map
# import math
# import json
# from typing import Callable
#
from sqlalchemy import Column, Integer, Float, Text, String
# from sqlalchemy.ext.declarative import declarative_base
# import chuck_pyutils.core as utils
# from sqlalchemy.orm import sessionmaker
#
from sqlalchemy import Column, DateTime, Float, Integer, String, UnicodeText
#
# Base = declarative_base()
# config = utils.read_config(utils.get_file_path(__file__, "config.ini"))
# from sqlalchemy import create_engine
#
# engine = create_engine(config["DATABASE"]["CONNECTION_STR"])
#
# class BaseModel(db.Model):
#     __abstract__ = True
#
#     @staticmethod
#     def create(new_entry):
#         try:
#             db.session.add(new_entry)
#             db.session.commit()
#             return new_entry.id
#         except Exception as e:
#             print("c", e)
#             return False
#
#     @classmethod
#     def read(cls, id_) -> Callable[..., "BaseModel"]:
#         return BaseModel.query.get(id_)
#
#     def update(self):
#         try:
#             db.session.commit()
#             return self.id
#         except Exception as e:
#             print("u", e)
#             return False
#
#     def delete(self):
#         try:
#             db.session.delete(self)
#             db.session.commit()
#             return self.id
#         except Exception as e:
#             print("d", e)
#             return False
#
#     @staticmethod
#     def object_dump(obj_name, obj_inst):
#         def dig_deep(prop_value):
#             dd_str = prop_value
#             if (
#                 type(prop_value).__str__ is object.__str__
#                 and not isinstance(prop_value, str)
#                 and not isinstance(prop_value, dict)
#             ):
#                 dd_str = BaseModel.object_dump(
#                     prop_value.__class__.__name__, prop_value
#                 )
#             return str(dd_str)
#
#         obj_vars = sorted(
#             [
#                 x
#                 for x in tuple(set(obj_inst.__dict__))
#                 if not x.startswith("__") and not x.startswith("_sa_instance_state")
#             ]
#         )
#         return "{}({})".format(
#             obj_name,
#             ", ".join(
#                 [
#                     "{}={}".format(var, dig_deep(getattr(obj_inst, var)))
#                     for var in obj_vars
#                 ]
#             ),
#         )
#
#     def __repr__(self):
#         obj_vars = sorted(
#             [
#                 x
#                 for x in tuple(set(self.__dict__))
#                 if not x.startswith("__") and x != "_sa_instance_state"
#             ]
#         )
#         return f'{self.__class__.__name__}({", ".join([f"{var}={getattr(self, var)}" for var in obj_vars])})'
#
#     def serialize(self):
#         return {
#             key: value
#             for key, value in self.__dict__.items()
#             if not key.startswith("_") and key != "metadata"
#         }
#
#
#
#
#
#
# class BuckEntry(BaseModel):
#     __tablename__ = "buck_entries"
#     id = Column(Integer, primary_key=True, unique=True)
#     fk_serial_number = Column(String(256), nullable=False)
#     zip_code = Column(String(256))
#     notes = Column(UnicodeText)
#     lat = Column(Float)
#     long = Column(Float)
#     timestamp = Column(DateTime)
#
#     @classmethod
#     def read(cls, id_) -> "BuckEntry":
#         return BuckEntry.query.get(id_)
#
#
# class BuckOwners(BaseModel):
#     __tablename__ = "buck_owners"
#     id = Column(Integer, primary_key=True, unique=True)
#     serial_number = Column(String(256), nullable=False)
#     owner_name = Column(String(256), nullable=False)
#
#     @classmethod
#     def read(cls, id_) -> "BuckOwners":
#         return BuckOwners.query.get(id_)
#
#
# # Create all tables in the engine. This is equivalent to "Create Table"
# # statements in raw SQL.
# # Base.metadata.create_all(engine)
# # Session = sessionmaker(bind=engine)
# # session = Session()
#
# # with open("../data/chuckratesbeer.json", "r") as data:
# #     for index, beer in enumerate(json.loads(data.read())):
# #         crb = ChuckRatesBeers()
# #         crb.bid = beer["bid"]
# #         crb.beer_name = beer["beer_name"]
# #         crb.brewery_name = beer["brewery_name"]
# #         crb.chuck_rating = float(beer["rating_score"])
# #         session.add(crb)
# #     session.commit()
#
#

import math

from sqlalchemy import create_engine, select
import configparser
from sqlalchemy.orm import Session
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass


class BuckEntry(Base):
    __tablename__ = "buck_entries"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    fk_serial_number: Mapped[str] = mapped_column(String(256), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(256))
    notes: Mapped[str] = mapped_column(UnicodeText)
    lat: Mapped[float] = mapped_column(Float)
    long: Mapped[float] = mapped_column(Float)
    timestamp = Column(DateTime)


# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# Create a configparser object
config = configparser.ConfigParser()

# Read the config file
config.read('../config.ini')

# Get the database credentials
host = config['DATABASE']['CONNECTION_STR']
def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculates the distance between two points on a sphere.

    Args:
    lat1: The latitude of the first point in degrees.
    lon1: The longitude of the first point in degrees.
    lat2: The latitude of the second point in degrees.
    lon2: The longitude of the second point in degrees.

    Returns:
    The distance between the two points in kilometers.
    """

    R = 6371 # The radius of the Earth in kilometers.
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    return R * c

def kilometers_to_miles(kilometers):
    """Converts kilometers to miles.

    Args:
    kilometers: The number of kilometers to convert.

    Returns:
    The number of miles.
    """
    return kilometers * 0.621371

# Create an engine to connect to the database
engine = create_engine(host)
# Create a connection to the database
# connection = engine.connect()
# print(connection)

# Create a cursor to execute SQL queries
# cursor = connection.cursor()
session = Session(engine)
total_distance = 0
longest_single_point_to_point = 0
longest_total_single_buck = 0
total_entries = 0
total_unique_dollars_checked_in = 0
largest_number_of_check_ins = 0
longest_single_point_to_point_sn = None
stmt = select(BuckEntry.fk_serial_number).distinct(BuckEntry.fk_serial_number)
y = session.scalars(stmt).fetchall()
z = len(y)
distance_dict = {}
for sn in y:
    distance_dict[sn] = 0
    # print(sn)
for sn in distance_dict.keys():
    new_s = select(BuckEntry).where(BuckEntry.fk_serial_number == sn)
    prev_lat = None
    prev_long = None
    x = session.scalars(new_s).fetchall()
    if len(x) != 1:
        for entry in x:
            if prev_lat:
                distance = haversine_distance(prev_lat, prev_long, entry.lat, entry.long)
                if max(longest_single_point_to_point, distance) == distance:
                    longest_single_point_to_point = distance
                    longest_single_point_to_point_sn = sn
                distance_dict[sn] += distance
            prev_lat = entry.lat
            prev_long = entry.long
print(distance_dict)
  # print(user.lat, user.long)
# Execute a SQL query
# connection.execute('SELECT * FROM flewloon.buck_entries;')

# Fetch the results of the query
# results = cursor.fetchall()

# Print the results of the query
# for row in results:
#     print/(row)

# Close the connection to the database
# connection.close()
longest_total_single_buck_sn = None

for k, v in distance_dict.items():
    total_distance += v
    if max(longest_total_single_buck, v) == v:
        longest_total_single_buck = v
        longest_total_single_buck_sn = k
    longest_total_single_buck = max(longest_total_single_buck, v)
total_unique_dollars_checked_in = y
    # largest_number_of_check_ins = max(largest_number_of_check_ins, len(x))
    # total_entries += len(x)

print(f"Total distance traveled: {total_distance} km")
print(f"Total distance traveled: {kilometers_to_miles(total_distance)} miles")
print(f"Longest single point to point: {longest_single_point_to_point_sn}")
print(f"Longest single point to point: {longest_single_point_to_point} km")
print(f"Longest single point to point: {kilometers_to_miles(longest_single_point_to_point)} miles")
print(f"Longest total single buck: {longest_total_single_buck_sn}")
print(f"Longest total single buck: {longest_total_single_buck} km")
print(f"Longest total single buck: {kilometers_to_miles(longest_total_single_buck)} miles")
print(f"Total unique dollars checked in: {len(total_unique_dollars_checked_in)}")


