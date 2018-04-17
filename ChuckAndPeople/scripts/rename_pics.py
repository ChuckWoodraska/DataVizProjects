import json
import os
import shutil
from datetime import datetime

# INSTAGRAM
with open('../data/picture_data.json', 'r') as data_file:
    pic_data = json.loads(data_file.read())
count = 365
for item in pic_data:
    shutil.copy('../../chuckwoodraska/{}'.format(item['display_url'].split('/')[-1]),
                '../data/cap/Day{}.jpg'.format(count))
    count -= 1

# GOOGLE PHOTOS
pic_list = os.listdir('../data/cap')
for item in pic_list:
    shutil.copy('../data/cap/{}'.format(item),
                '../data/cap_pics/Day{}.jpg'.format(
                    datetime.strptime(item.split('_')[1], '%Y%m%d').timetuple().tm_yday))
