import csv
from csv import DictReader
with open('c.csv' ,mode='r') as f:
    file=DictReader(f)
    for x in file:
        print(x['Letter'])