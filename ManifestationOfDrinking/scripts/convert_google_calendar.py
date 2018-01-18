import csv
import calendar

input_file = csv.DictReader(open("mod.csv", 'rU'), dialect=csv.excel_tab)

total_drink_dict = {'Guinness': 0, 'md': 0, 'shot': 0, 'beer': 0}
monthly_drink_dict = {}
output_list = []

for row in input_file:
    drink_list = row['Title'].split(':')
    date_str = row["Given planned earliest start"].split("/")[2] + "-" + \
               row["Given planned earliest start"].split("/")[0] + "-" + \
               row["Given planned earliest start"].split("/")[1]
    month = row["Given planned earliest start"].split("/")[0]
    if month not in monthly_drink_dict:
        monthly_drink_dict[month] = {'Guinness': 0, 'md': 0, 'shot': 0, 'beer': 0}
    total = 0
    for drink in drink_list:

        drink = drink.strip()
        drink_count_list = drink.split()
        drink_name = drink_count_list[1]
        if drink_name in drink:
            try:
                total_drink_dict[drink_name] += int(drink_count_list[0])
                total += int(drink_count_list[0])
                monthly_drink_dict[month][drink_name] += int(drink_count_list[0])
            except KeyError:
                total_drink_dict[drink_name[:-1]] += int(drink_count_list[0])
                total += int(drink_count_list[0])
                monthly_drink_dict[month][drink_name[:-1]] += int(drink_count_list[0])
        else:
            print(drink_count_list[1])
    output_list.append({"Date": date_str, "Title": row['Title'], "Total": total})
print("Total Guinness: {guinness}\n" \
      "Total Beers: {beer}\n" \
      "Total Mixed Drinks: {md}\n" \
      "Total Shots: {shot}\n".format(guinness=total_drink_dict["Guinness"],
                                     beer=total_drink_dict["beer"],
                                     md=total_drink_dict["md"],
                                     shot=total_drink_dict["shot"]))

for month_key in sorted(monthly_drink_dict):
    print("Month: {month}\n" \
          "Guinness: {guinness}\n" \
          "Beers: {beer}\n" \
          "Mixed Drinks: {md}\n" \
          "Shots: {shot}\n".format(month=calendar.month_name[int(month_key)],
                                   guinness=monthly_drink_dict[month_key]["Guinness"],
                                   beer=monthly_drink_dict[month_key]["beer"],
                                   md=monthly_drink_dict[month_key]["md"],
                                   shot=monthly_drink_dict[month_key]["shot"]))

with open('modd3.csv', 'wb') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, output_list[0].keys())
    w.writeheader()
    w.writerows(output_list)
