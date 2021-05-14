import csv

l_l = ["data3"]
total = 0
with open('../data/steps.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        if row[0] != 'Date':
            total += int(row[1])
            l_l.append(total)

print(l_l)