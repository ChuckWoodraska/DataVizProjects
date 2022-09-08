import json

pic_dict = {}
with open('../data/main/main.json', 'r') as a:
    a = json.loads(a.read())

    for item in a:
        s = int(item[0].split('/')[-1][:-4].split('Day')[1])
        pic_dict[s] = pic_dict[s] + 1 if pic_dict.get(s) else 1
pic_dict['mosaic_tile_stat_str'] = '{}/365 ({:.2f}%)'.format(len(pic_dict), len(pic_dict)/365*100)
for x in range(1, 366):
    if x not in pic_dict:
        pic_dict[x] = 0
with open('../data/main_all.json', 'w') as a:
    a.write(json.dumps(pic_dict))

mosaic_dict = {}
total_pic_dict = {}
max_percent = 0
max_percent_day = 0
min_percent = 366
min_percent_day = 0
for x in range(1, 366):
    pic_dict = {}
    with open(f'../data/mosaic_json/Day{x}.json', 'r') as a:
        a = json.loads(a.read())

        for item in a:
            s = int(item[0].split('/')[-1][:-4].split('Day')[1])
            pic_dict[s] = pic_dict[s] + 1 if pic_dict.get(s) else 1
            s = int(item[0].split('/')[-1][:-4].split('Day')[1])
            total_pic_dict[s] = total_pic_dict[s] + 1 if total_pic_dict.get(s) else 1
    pic_dict['mosaic_tile_stat_str'] = '{}/365 ({:.2f}%)'.format(len(pic_dict), len(pic_dict) / 365 * 100)
    if len(pic_dict) > max_percent:
        max_percent = len(pic_dict)
        max_percent_day = x
    if len(pic_dict) < min_percent:
        min_percent = len(pic_dict)
        min_percent_day = x
    for y in range(1, 366):
        if y not in pic_dict:
            pic_dict[y] = 0
    mosaic_dict[x] = pic_dict

print(total_pic_dict[max(total_pic_dict, key=total_pic_dict.get)])
print(total_pic_dict[min(total_pic_dict, key=total_pic_dict.get)])
print(max(total_pic_dict, key=total_pic_dict.get))
print(min(total_pic_dict, key=total_pic_dict.get))
print(max_percent)
print(min_percent)
print(max_percent_day)
print(min_percent_day)

with open('../data/mosaic_all.json', 'w') as a:
    a.write(json.dumps(mosaic_dict))

progressive_dict = {}
for x in range(1, 366):
    pic_dict = {}
    with open(f'../data/progressive_json/Day{x}.json', 'r') as a:
        a = json.loads(a.read())

        for item in a:
            s = int(item[0].split('/')[-1][:-4].split('Day')[1])
            pic_dict[s] = pic_dict[s] + 1 if pic_dict.get(s) else 1
    pic_dict['progressive_tile_stat_str'] = '{}/365 ({:.2f}%)'.format(len(pic_dict), len(pic_dict)/365*100)
    for y in range(1, 366):
        if y not in pic_dict:
            pic_dict[y] = 0
    progressive_dict[x] = pic_dict

with open('../data/progressive_all.json', 'w') as a:
    a.write(json.dumps(progressive_dict))
