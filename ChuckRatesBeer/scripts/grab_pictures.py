import requests
import json

url = "https:\/\/untappd.s3.amazonaws.com\/photo\/2018_01_01\/c3c00c65cb3f75877281caaab576f4e2_raw.jpeg"

with open("../data/chuckratesbeer.json", "r") as data:
    for index, beer in enumerate(json.loads(data.read())):
        print(index, beer)
        r = requests.get(beer.get("photo_url"))

        if r.status_code == 200:
            with open("../data/pics_raw/Day{}.jpg".format(index+1), 'wb') as f:
                f.write(r.content)
        # break

# url = url.replace("\/", "/")
# print(url)
# filename = url.split("/")[-1]
# r = requests.get(url, timeout=0.5)
#
# if r.status_code == 200:
#     with open(filename, 'wb') as f:
#         f.write(r.content)