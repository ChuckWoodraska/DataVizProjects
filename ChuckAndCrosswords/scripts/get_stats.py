# take string in form of "MM:SS" and return number of seconds
import itertools


def get_seconds(time):
    minutes, seconds = time.split(":")
    return int(minutes) * 60 + int(seconds)


days_dict = dict.fromkeys(range(1, 365), {"grid15": {"num_correct": 0, "num_blank": 0, "num_wrong": 0}, "grid30": {"num_correct": 0, "num_blank": 0, "num_wrong": 0}, "grid45": {"num_correct": 0, "num_blank": 0, "num_wrong": 0}})
# make dict for days of the week with the key being the day of the week and the value 0
dow_dict = dict.fromkeys(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], {"max": "", "min": "", "avg": 0})

# make dict for months with the key being the month and the value 0
month_dict = dict.fromkeys(range(1, 13), {"max": "", "min": "", "avg": 0})

# percentages per puzzle
# most common words
# use counter to count the number of times a word appears in the list
from collections import Counter
count = Counter([
      "HIJACKS",
      "ASSN",
      "QUE",
      "IFORONE",
      "SPAY",
      "UND",
      "PSYCHOACTIVE",
      "EPI",
      "HOTSAUCE",
      "FEET",
      "MBA",
      "OTTER",
      "ERRS",
      "POLEDANCED",
      "ARESO",
      "GOLDRUSH",
      "UPTOYOU",
      "GED",
      "20PERCENT",
      "FOREVER21",
      "REI",
      "EVELINE",
      "APPSTORE",
      "REVEL",
      "SOLASTYEAR",
      "GROS",
      "DEBUG",
      "RNA",
      "URLS",
      "OATMEALS",
      "SIT",
      "APLUSAVERAGE",
      "ODE",
      "SEES",
      "NOTICES",
      "NED",
      "HYDE",
      "TWOSTEP"
    ])

print(count.most_common(10))