class student:
    def __init__(self,name,age,cgpa,uni):
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.uni = uni
    def display(self):
        print("name: ",self.name)
        print("age:",self.age)
        print("cgpa: ", self.cgpa)
        print("university: ",self.uni)
student1 = student("ali", 23, 3.5,"uet")
student2 = student("abrar", 26, 3.2,"umt")
student1.display()
student2.display()
