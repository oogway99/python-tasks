import math
import random
from datetime import datetime, date
import time
import csv
## part A

# find the sq. root of 144
square_root = math.sqrt(144)
print (square_root)

# Find 7⁴ using math.pow()
power = math.pow(7,4)
print (power)

#Print the value of math.pi
print (math.pi)

#Calculate the area of a circle with a radius of 10
r = 10
area = (math.pi)*r**2
print (area)

## part B

# Generate a random number between 50 and 100
number = (random.randint(51,99))
print (number)

#Generate a 6-digit OTP
otp = random.randint(100000,999999)
print (otp)

#Create a list of five fruits and randomly print one fruit using random.choice()
fruits = ['apple', 'mango', 'banana', 'grapefruit', 'watermelon']
print (random.choice(fruits))

## part C

#Print the current date and time
print(datetime.now())

#Print today's date only
print(date.today())

#Display the message "Program Started", wait for 3 seconds, then display "Program Finished"
print ('program started')
time.sleep(3)
print ('program finished')

## part D
# file 1 

# reading practice.csv
with open('practice.csv', 'r') as file:
     contains = csv.reader(file)
 # print all records
     for row in contains:
        print (row)

# applying 4 conditions
# condition 1
    for row in contains:
        if "B" in row[1] and "f_50-99" in row[3]:
            print (row)
# conditin 2 
        if "Electricity, Gas, Water and Waste Services" in row[2] and "2011" in row[0]:
            print (row)
#  condition 3
        value = row[5]
        if value == "C" or value == "value": #these strings were not allowing the conversion of value to int type
            continue
        value = int (value)
        if value <= 1000:
            print (row)
# condition 4
        if "Fixed tangible assets" in row[4]:
            print (row)

## file 2

# reading csv1.csv
with open('csv1.csv', 'r') as file:
    contains = csv.reader(file)
# print all records
    for row in contains:
         print (row)

# applying 4 conditions
# condition 1
        if "REVISED" in row[4]:
            print (row)
# conditin 2 
        if "2023.03" in row[0] and "REVISED" in row[4]:
            print (row)
#  condition 3
        value = row[2]
        if value == 'Data_value':
            continue
        value = int (value)
        if value <= 100:
            print (row)
# condition 4
        if "All control" in row[10] and "REVISED" in row[4]:
            print (row)

## file 3

# reading csv2.csv
with open('csv2.csv', 'r') as file:
    contains = csv.reader(file)
## print all records
    for row in contains:
        print (row)

# applying 4 conditions
# condition 1
        if "Agriculture" in row[2]:
            print (row)
# conditin 2 
        if "Agriculture" in row[2] and "Actual" in row[4]:
            print (row)
#  condition 3
        value = row[6]
        if value == 'Data_value':
            continue
        value = int (value)
        if value <= 100:
            print (row)
# condition 4
        if "ZGZ" in row[1] and "2015.03" in row[0]:
            print (row)
