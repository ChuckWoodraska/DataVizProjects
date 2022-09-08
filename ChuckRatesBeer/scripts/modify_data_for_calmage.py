import json

new_dict = {}

with open("../data/chuckratesbeer.json", "r") as data:
    for index, beer in enumerate(json.loads(data.read())):
        new_dict[f'Day{index + 1}'] = {
            'beer_name': beer['beer_name'],
            'brewery_name': beer['brewery_name'],
            'untappd_url': beer['checkin_url'],
        }

    with open("../data/crb_by_day.json", 'w') as f:
        f.write(json.dumps(new_dict))
