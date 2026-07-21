## task 1
# CREATING A FILE and writing it
with open("assignment_06\student.txt", "w") as file:
    file.write("Rameen \nMphil-Math \nUET")

## task 2
# Read the contents of student.txt and display them on the screen:
with open("assignment_06\student.txt", "r") as file:
    print(file.read())                                # reads whole file
with open("assignment_06\student.txt", "r") as file:
    print(file.readline())                            # read first line
with open("assignment_06\student.txt", "r") as file:
    print(file.readlines())                           # read all lines

## task 3
# appending data
with open("assignment_06\student.txt", "a") as file:
    file.write("\nCourse: Python Programming")
# displaying appended data
with open("assignment_06\student.txt", "r") as file:
    print(file.read())

## task 4 
# handle division error 
try:
    num_1 = int(input("enter num_1 = "))
    num_2 = int(input("enter num_2 = "))
    division = num_1/num_2
    print ("quotient is = " , division)
except ZeroDivisionError:
    print ("nothing can be divided by zero")

## task 5
# Handle Invalid Input
try:
    age = int(input("Enter your age = "))
except ValueError:
    print("Please enter a valid number")

## task 6
# Use else and finally
try:
    num_1 = int(input("enter a number = "))
    square = (num_1**2)
except:
    print ("Please enter a valid number")
else:
    print ("square is = ", square)
finally:
    print ("program finished")

## task 7
# Mini Project
try:
    name = input("Enter your name: ")
    marks = int(input("Enter obtained marks: "))
    if marks < 0 or marks > 100:
        print ("invalid marks")
except ValueError:
    print ("Please enter a valid number")
else:
    if marks in range(0,101):
        print ("Student name: ", name)
        print("Obtained Marks: ", marks)
    grade = {
        "A":range(85,101),
        "B":range(70,85),
        "C":range(50,70),
        "F":range(0,50)
        }
    for key,values in grade.items():
        if marks in values:
            print ("Grade: ",key)
