import json
pic_dict = {}
with open('../data/mosaic_json/Day1.json', 'r') as a:
    a = json.loads(a.read())

    for item in a:
        s = int(item[0].split('/')[-1][:-4].split('Day')[1])
        if pic_dict.get(s):
            pic_dict[s] = pic_dict[s] + 1
        else:
            pic_dict[s] = 1
