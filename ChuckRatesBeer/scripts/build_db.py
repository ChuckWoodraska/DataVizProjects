import requests
import json

with open("../data/chuckratesbeer.json", "r") as data:
    for index, beer in enumerate(json.loads(data.read())):
        print(index, beer)
        r = requests.get(beer.get("photo_url"))

        if r.status_code == 200:
            with open("../data/pics_raw/Day{}.jpg".format(index+1), 'wb') as f:
                f.write(r.content)
