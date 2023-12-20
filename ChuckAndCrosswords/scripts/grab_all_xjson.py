import requests
from datetime import timedelta, datetime
import os

YEAR = 2021
headers = {

}

day = datetime(YEAR, 1, 1)


while day.year == YEAR:
    lookup_day = day.strftime("%m/%d/%Y")
    r = requests.get(f"https://www.xwordinfo.com/JSON/Data.ashx?date={lookup_day}&format=text", headers=headers)
    if r.status_code == 200:
        filename = f"../data/{day.month:02}/{day.day:02}.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(r.text)
    else:
        print(lookup_day)
    day = day + timedelta(1)
    print(f"passed: {lookup_day}")

