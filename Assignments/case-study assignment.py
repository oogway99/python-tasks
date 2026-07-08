marks = [78,85,-5,92,67,100,88,45]
# display valid marks
for i in marks:
    if i > 0:
     print (i)
print("valid marks: ")
# skip invalid marks
for i in marks:
    if i == -5:
       continue
    print (i)
print ("valid marks = ")
# stop when perfect score is found of valid data
for i in marks:
    if i==-5:
     continue
    if i == 100:
       break
    print (i)
print ("perfect score found")    
