# making calculator
x= float(input ("enter num_1 = "))
y= float(input ("enter num_2 = "))
z= input("select the operator from +,-,*,/ ")
if z == "+":
    print ("sum is ", x+y)
elif z == "-":
    print ("difference is ", x-y)
elif z == "*":
    print ("product is ", x*y)
elif z == "/":
    if y != 0 :
        print ("quotient is ", x/y)
    else:
        print ("math error")
else:
    print ("not possible")
