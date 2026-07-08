
import math
import csv
with open('practice.csv', 'r') as file:
    contains = csv.reader(file)
    for row in contains:
        value = row[5]
        if value == "C" or value == "value": #these strings were not allowing the conversion of value to int type
            continue
        value = int (value)
        if value <= 1000:
            print (row)

        # if "B" in col[1] and "f_50-99" in col[3]:
        # if "Electricity, Gas, Water and Waste Services" in col[2] and "2011" in col[0]:
