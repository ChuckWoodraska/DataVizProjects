# for i in range(1114):
#     print('<div id="map{}" style="width:700px; height:500px; margin-left:80px;"></div>'.format(i+1))
import tcxparser
import json
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from pathlib import Path
import configparser

pathlist = Path("../data/2019-Google").glob('*.tcx')
count = 1
# with open('output.txt', 'w') as f:
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
#                 flightPath.setMap(map{});
#
#               """.format(count, count, {"lat": pv[0][0], "lng": pv[0][1]}, new_dict, count)
#             f.write(maps)
#         count += 1
#         if count == 100:
#             break