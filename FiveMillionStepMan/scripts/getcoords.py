import tcxparser
import json
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from pathlib import Path
import configparser
import datetime
import csv
from dateutil.parser import parse

Base = declarative_base()

def db_connect(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    db_conn_str = config['DATABASE']['CONNECTION_STR']
    return create_engine(db_conn_str)


class ChuckSteps(Base):
    __tablename__ = 'chuck_steps2'
    id = Column(Integer, primary_key=True, unique=True)
    duration = Column(Integer)
    distance = Column(Integer)
    position_values = Column(JSON)
    start_lat = Column(Float, nullable=False)
    start_long = Column(Float, nullable=False)
    end_lat= Column(Float, nullable=False)
    end_long = Column(Float, nullable=False)
    median_lat = Column(Float, nullable=False)
    median_long = Column(Float, nullable=False)
    route_name_id = Column(Integer)
    file_name = Column(String(512))
    timestamp = Column(DateTime)
    shorty_values = Column(JSON)
    sv2 = Column(JSON)
#
# class RouteNames(Base):
#     __tablename__ = 'route_names'
#     id = Column(Integer, primary_key=True, unique=True)
#     route_name = Column(String(256), nullable=False)
#     example_id = Column(Integer)
#
class RealSteps(Base):
    __tablename__ = 'real_steps'
    id = Column(Integer, primary_key=True, unique=True)
    step_count = Column(Integer, nullable=False)
    steps_timestamp = Column(DateTime)

def main6():
    engine = db_connect()
    session = sessionmaker(bind=engine)()
    results = session.query(ChuckSteps).all()
    with open('output.txt', 'w') as f:
        for result in results:
            fp = """
                    var flightPlanCoordinates = {};
                    var flightPath = new google.maps.Polyline({{
                      path: flightPlanCoordinates,
                      geodesic: true,
                      strokeColor: '#FF0000',
                      strokeOpacity: 1.0,
                      strokeWeight: 5
                    }});

                    flightPath.setMap(map1);
                  """.format(result.sv2)
            f.write(fp)


#
#     for path in pathlist:
#         # because path is object not string
#         path_in_str = str(path)
#         # with open(path_in_str, "r") as data/:
#         a = tcxparser.TCXParser(path_in_str)
#         pv = a.position_values()
#         if pv:
#             # print(a.started_at)
#             # print(pv[-1])
#             # print(pv[0])
#             # print(pv[int(len(pv)/2)])
#             # print(int(a.duration))
#             # print(int(a.distance))
#
#             new_dict = []
#             for v in a.position_values():
#                 new_dict.append({"lat": v[0], "lng": v[1]})
#
#             maps = """        var map{} = new google.maps.Map(document.getElementById('map{}'), {{
#                   zoom: 15,
#                   center: {},
#                   mapTypeId: google.maps.MapTypeId.ROADMAP
#                 }});
#
#                 var flightPlanCoordinates = {};
#                 var flightPath = new google.maps.Polyline({{
#                   path: flightPlanCoordinates,
#                   geodesic: true,
#                   strokeColor: '#FF0000',
#                   strokeOpacity: 1.0,
#                   strokeWeight: 5
#                 }});
#
#
#
#               """.format(count, count, {"lat": pv[0][0], "lng": pv[0][1]}, new_dict, count)
#             f.write(maps)
def main5():
    engine = db_connect()
    session = sessionmaker(bind=engine)()
    results = session.query(ChuckSteps).all()
    for result in results:
        if len(result.position_values) <= 100:
            result.sv2 = result.position_values
        else:
            result.sv2 = result.position_values[::10]
        session.commit()

def main4():
    engine = db_connect()
    session = sessionmaker(bind=engine)()
    results = session.query(ChuckSteps).all()
    # for result in results:


def main3():
    engine = db_connect()
    session = sessionmaker(bind=engine)()
    results = session.query(ChuckSteps).all()
    for result in results:
        print(result.id, result.file_name)
        date_path = result.file_name.split('/')[3].split('_PT')[0]
        datett = date_path.replace('_', ':')
        print(datett)
        datt = parse(datett)
        my_date = datetime.datetime.utcfromtimestamp(datt.timestamp())
        result.timestamp = my_date
        session.commit()
        # print(repr(datetime.datetime.utcfromtimestamp(datt.timestamp())))

def endo_main():
    pathlist = Path("../data/2019-Endomondo").iterdir()
    count = 0
    engine = db_connect()
    session = sessionmaker(bind=engine)()
    results = session.query(ChuckSteps).all()
    print(results)
    for path in sorted(pathlist):
    #          because path is object not string
        path_in_str = str(path)
        print(path_in_str)
        # with open(path_in_str, "r") as data/:
        a = tcxparser.TCXParser(path_in_str)
        pv = a.position_values()
        if pv and "Basketball" not in path_in_str:
            date_path = path_in_str.split('/')[3].split('.tcx')[0]
            print(date_path)
            #     date_path = path_in_str.split('/')[3].split('_PT')[0]
            #     datett = date_path.replace('_', ':')
            datt = parse(date_path)
            print(datt)
            #     print(repr(datetime.datetime.utcfromtimestamp(datt.timestamp())))
            tmp_ll_json = [{"lat": ll[0], "lng": ll[1]} for ll in pv]
            # # pass
            total_distance = sum(a.distance_values())
            total_duration = sum(a.duration_values())
            # # print([a.distance_values())
            new_cs = ChuckSteps()
            new_cs.duration = int(total_duration)
            new_cs.distance = int(total_distance)
            new_cs.position_values = tmp_ll_json
            new_cs.start_lat = pv[0][0]
            new_cs.start_long = pv[0][1]
            new_cs.end_lat = pv[-1][0]
            new_cs.end_long = pv[-1][1]
            mid_pv = len(pv) // 2
            new_cs.median_lat = pv[mid_pv][0]
            new_cs.median_long = pv[mid_pv][1]
            new_cs.route_name_id = None
            new_cs.file_name = path_in_str
            new_cs.timestamp = datt
            if len(new_cs.position_values) <= 100:
                new_cs.sv2 = new_cs.position_values
            else:
                new_cs.sv2 = new_cs.position_values[::10]
            session.add(new_cs)
            session.commit()
                    # count += 1
        else:
            print(path_in_str)

            # new_dict = []
            # for v in a.position_values():
            #     new_dict.append({"lat": v[0], "lng": v[1]})
            # print(a.activity_type)
        # print(a.position_values())
        # new_dict = []
        # for v in a.position_values():
        #     new_dict.append({"lat": v[0], "lng": v[1]})
        # print(json.dumps(new_dict))
        # print(path_in_str)

def main():
    pathlist = Path("../data/2019-Endomondo").iterdir()
    count = 0
    engine = db_connect()
    session = sessionmaker(bind=engine)()
    results = session.query(ChuckSteps).all()
    print(results)
    for path in sorted(pathlist):
    #          because path is object not string
        path_in_str = str(path)
        print(path_in_str)
        # with open(path_in_str, "r") as data/:
        a = tcxparser.TCXParser(path_in_str)
        pv = a.position_values()
        if pv and "Basketball" not in path_in_str:
        #     date_path = path_in_str.split('/')[3].split('_PT')[0]
        #     datett = date_path.replace('_', ':')
        #     datt = parse(datett)
        #     print(repr(datetime.datetime.utcfromtimestamp(datt.timestamp())))
            tmp_ll_json = [{"lat": ll[0], "lng": ll[1]} for ll in pv]
                    # # pass
                    # total_distance = 0
                    # for v in a.distance_values():
                    #     total_distance += v
                    # total_duration = 0
                    # for v in a.duration_values():
                    #     total_duration += v
                    # # print([a.distance_values())
                    # new_cs = ChuckSteps()
                    # new_cs.duration = int(total_duration)
                    # new_cs.distance = int(total_distance)
                    # new_cs.position_values = tmp_ll_json
                    # new_cs.start_lat = pv[0][0]
                    # new_cs.start_long = pv[0][1]
                    # new_cs.end_lat = pv[-1][0]
                    # new_cs.end_long = pv[-1][1]
                    # mid_pv = int(len(pv)/2)
                    # new_cs.median_lat = pv[mid_pv][0]
                    # new_cs.median_long = pv[mid_pv][1]
                    # new_cs.route_name_id = None
                    # new_cs.file_name = path_in_str
                    # session.add(new_cs)
                    # session.commit()
                    # count += 1
        else:
            print(path_in_str)

            # new_dict = []
            # for v in a.position_values():
            #     new_dict.append({"lat": v[0], "lng": v[1]})
            # print(a.activity_type)
         # print(a.position_values())
         # new_dict = []
         # for v in a.position_values():
         #     new_dict.append({"lat": v[0], "lng": v[1]})
         # print(json.dumps(new_dict))
         # print(path_in_str)
    # with open("../data/chuckratesbeer.json", "r") as data:
    # a = tcxparser.TCXParser("tt.tcx")
    # new_dict = []
    # for v in a.position_values():
    #     new_dict.append({"lat": v[0], "lng": v[1]})
    # print(json.dumps(new_dict))

    # print(count)

def main2():
    engine = db_connect()
    Base.metadata.create_all(engine)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
# engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
# Base.metadata.create_all(engine)
# new_dict = {}
#
# with open("../data/chuckratesbeer.json", "r") as data:
#     for index, beer in enumerate(json.loads(data.read())):
#         new_dict['Day{}'.format(index + 1)] = {'beer_name': beer['beer_name'],
#                                                'brewery_name': beer['brewery_name'],
#                                                'untappd_url': beer['checkin_url']}
#     with open("../data/crb_by_day.json", 'w') as f:
#         f.write(json.dumps(new_dict))
#
# class ChuckRatesBeers(BaseModel):
#     __tablename__ = "chuck_rates_beers"
#     id = db.Column(
#         "id", db.Integer, primary_key=True, unique=True, index=True, autoincrement=True
#     )
#     bid = db.Column("bid", db.Integer,)
#     abv = db.Column("abv", db.Integer,)
#     ibu = db.Column("ibu", db.Integer,)
#     global_rating = db.Column("global_rating", db.Integer, )
#     chuck_rating = db.Column("chuck_rating", db.Integer,)

def main10():
    engine = db_connect()
    session = sessionmaker(bind=engine)()
    with open('../data/steps.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row)

            if row[0] != 'Date':
                dt = parse(row[0])
                # print(dt)
                new_rs = RealSteps()
                new_rs.steps_timestamp = dt
                new_rs.step_count = row[1]
                session.add(new_rs)
                session.commit()


# main10()
# main2()
endo_main()