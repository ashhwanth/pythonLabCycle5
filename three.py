import csv
with open('c.csv', mode='r')as f:
    file=csv.reader(f)
    for x in file:
        print(x)
