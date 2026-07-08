# unit-converter without using if-else conditions
num = float(input("enter the value:"))
print ("km to m ", num*1000) 
print ("m to km ", num/1000)
print ("in to cm ", num*2.54)
print ("cm to in ", num/2.54)
print ("m to ft ", num/0.3048)
print ("ft to m ", num*0.3048)
print ("miles to km ", num*1.60934)
print ("km to miles ", num/1.60934)

# simple conversion  of temp
x = float (input(" enter the value =") )
print ("celsius to fahrenheit", (x*(9/5)+32 ))
print ("fahrenheit to celsius", ((x-32)*(5/9)))

# temperature conversion using if else
x = float (input(" enter the value =") )
y = input("which conversion do you want C or F = ")
if y == "C" or y == "c":
    print ("fahrenheit to celsius", ((x-32)*(5/9)))
elif y == "F" or y =="f":
        print ("celsius to fahrenheit", (x*(9/5)+32 ))
else:
    print ("sorry can't proceed")
