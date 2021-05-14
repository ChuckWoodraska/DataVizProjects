import csv
from datetime import datetime

total = 0
days_comp = 0
max_steps = 0
least_steps = 13000
dow_dict = {
    0: {"count": 0, "total": 0},
    1: {"count": 0, "total": 0},
    2: {"count": 0, "total": 0},
    3: {"count": 0, "total": 0},
    4: {"count": 0, "total": 0},
    5: {"count": 0, "total": 0},
    6: {"count": 0, "total": 0},
}
month_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
with open("../data/steps.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row)
        if row[0] != "Date":
            ds = datetime.strptime(row[0], "%m-%d-%y")
            weekday = ds.weekday()
            month = ds.month
            dow_dict[weekday]["count"] += 1
            dow_dict[weekday]["total"] += int(row[1])
            month_dict[month] += int(row[1])
            total += int(row[1])
            max_steps = max(max_steps, int(row[1]))
            least_steps = min(least_steps, int(row[1]))
            if int(row[1]) >= 13000:
                days_comp += 1
print(f"total: {total}")
print(f"avg steps per day: {total / 365}")
print(f"avg steps per week: {total / 52}")
print(f"avg steps per month: {total / 12}")
print(f"days completed: {days_comp}/365 {days_comp / 365}")
print(f"dow_dict: {dow_dict}")
for key, value in dow_dict.items():
    print(key, value["total"] / value["count"])
print(f"month_dic: {month_dict}")
print(f"most_steps: {max_steps}")
print(f"least_steps: {least_steps}")
print(f"most_steps: {max_steps * 365}")
print(f"least_steps: {least_steps * 365}")
