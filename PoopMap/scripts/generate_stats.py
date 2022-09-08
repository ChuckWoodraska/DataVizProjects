import pandas
import datetime
from geopy.distance import vincenty

frames = pandas.read_csv('E:\Data\poopmap\poopmap.csv')
iterdf = frames.iterrows()

max_days = 0
tmp_max_days = 1
consec_days = 0
tmp_consec_days = 0
prev_day = 0
max_dist = 0
dotw = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
marker_list = []
date_list = []
distance_list = []
distance_sum = 0
for row in iterdf:
    date = row[1]['Date']
    lat1 = row[1]['Lat']
    long1 = row[1]['Long']
    date_datetime = datetime.datetime.strptime(date, "%m/%d/%Y %H:%M")+datetime.timedelta(hours=1)
    date_list.append(f"'{date_datetime.strftime('%Y%m%d%H')}'")
    print("var marker{} = new google.maps.Marker({{\n\tposition: {{lat: {}, lng: {}}},\n\tmap: map,\n\ttitle: '{}'\n}});".format(row[0], lat1, long1, date_datetime.strftime("%b %d %Y #%H")))
    print("marker{0}.addListener('click', function() {{\n\tinfowindow.setContent(marker{0}.title);\n\tinfowindow.open(map, marker{0});\n}});".format(row[0]))
    marker_list.append(f'marker{row[0]}')
    dotw[date_datetime.weekday()] += 1
    distance_ab = vincenty((lat1, long1), (32.816220, -80.035723)).miles
    distance_sum += distance_ab
    distance_list.append(str(distance_ab))
    if date_datetime.timetuple().tm_yday - prev_day == 0:
        tmp_max_days += 1
        if tmp_max_days >= max_days:
            max_days = tmp_max_days
    elif date_datetime.timetuple().tm_yday - prev_day == 1:
        tmp_consec_days += 1
        if tmp_consec_days > consec_days:
            consec_days = tmp_consec_days
        tmp_max_days = 1
    else:
        tmp_consec_days = 0
        tmp_max_days = 1
    prev_day = date_datetime.timetuple().tm_yday
    lat2 = lat1
    long2 = long1
print(max_dist)
print(consec_days)
print(max_days)
print(dotw)
print(', '.join(marker_list))
print(', '.join(date_list))
print(', '.join(distance_list))
print(distance_sum/len(distance_list))