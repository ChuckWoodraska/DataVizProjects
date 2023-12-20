from datetime import timedelta, datetime
import os
import json

YEAR = 2021
headers = {

}

day = datetime(YEAR, 1, 1)


while day.year == YEAR:
    filename = f"../data/{day.month:02}/{day.day:02}.json"
    with open(filename, "r") as f:
        r = json.loads(f.read())
        grid_flags = None
        if r.get("dow") == "Sunday":
            if "grid15" in r and "grid30" in r and "grid45" in r:
                grid_flags = True
        else:
            if "grid15" in r and "grid30" in r:
                grid_flags = True
        print(f"{r.get('title')}, {r.get('dow')}, {grid_flags}, {r.get('time')}")
    day = day + timedelta(1)

