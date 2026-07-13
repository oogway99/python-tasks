## task 2 lists

import college as co
student_list = ['rameen','usama',"anas","wasiq","maryam"]

# displaying student list
print (co.display_students(student_list))
# adding a new student
student_list.append ("ahmad")
# remove one student
student_list.remove("usama")
# Update one student's name
student_list[1] = "muhammad usama"
# total students
total = co.total_students(student_list)

## task 3 tuples

data = ("bsf01","mathematics","2nd","bse876","english","7th","bsi43","islamiyat","6th","bsi2613","islamiyat","7th")
print(data[0])
print (data[1])
print (data[2])
print (data[3])
print (data[4])
print (data[5])
print (data[6])
print (data[7])
print (data[8])
print (data[9])
print (data[10])
print (data[11])
# modifying one value
data.append("fp234") # it gives error 

### this error is given because tuples are immutable  ###

## task 4 sets

club = {"drama","debate","sci and tech","bazm-e-adab","cosmology","debate"}
# display the set
print(co.display_students(club))
# add a new element
club.add("mathematics")
# remove an element
club.remove("drama")
# Check whether a club exists using the in operator
if "cosmology" in club:
    print (True)
else:
    print(False)

## task 5 final output
print (co.welcome())
print (co.display_students(student_list))
print (total)
print (co.display_students(data))
print (co.display_students(club))
