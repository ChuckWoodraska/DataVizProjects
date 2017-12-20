import csv
import json
import datetime

home = 0
away = 0
fastest = 100
slowest = 0
total = 0
tod_vs_speed_dict = {}
tod_list = ["tod"]
speed_list = ["speed"]
date_list = ["x"]
reader = csv.DictReader(open('../data/guinness.csv', 'r'))
for row in reader:
    # Home vs Other
    if int(row['AtHome']):
        home += 1
    else:
        away += 1

    # avg, total, fastest, slowest
    speed = int(row['Duration(Seconds)'])
    if speed < fastest:
        fastest = speed
    if speed > slowest:
        slowest = speed
    total += speed

    # time of day vs speed
    create_time = datetime.datetime.strptime(row['CreateDate'], '%Y-%m-%dT%H:%M:%S')
    tod = "{:02d}:{:02d}".format(create_time.hour, create_time.minute)
    tod_vs_speed_dict[row['ID']] = {'tod': tod,
                                    'speed': row['Duration(Seconds)']}
    tod_list.append(tod)
    speed_list.append(int(row['Duration(Seconds)']))
    date_list.append('{}-{:02d}-{:02d}'.format(create_time.year, create_time.month, create_time.day))

# Output
print(json.dumps(tod_vs_speed_dict))
print(json.dumps(tod_list))
print(json.dumps(speed_list))
print(home)
print(away)
print(fastest)
print(slowest)
print(total/60.0)
print(total/366.0)
print(json.dumps(date_list))
