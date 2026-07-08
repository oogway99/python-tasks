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
# Read the CSV file.
# Print all records.
# Apply at least 4 different filters using if statements.
# Print only the matching records for each filter.

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
