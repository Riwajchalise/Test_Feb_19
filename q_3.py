'''
Q3. Create a Student class and initialize it with name and roll number. Make methods to :
      a. Display - It should display all informations of the student.
      b. setAge - It should assign age to student
      c. setMarks - It should assign marks to the student.
'''

class Student:
    age =0
    marks =0

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def setage(self,age):
        self.age = age

    def setmarks(self,marks):
        self.marks = marks

    def display(self):
        return "name:{} - roll {} - age {} - marks {}.".format(self.name, self.roll, self.age, self.marks)


s1=Student(input("enter the name of student"),int(input("enter the roll number")))


Student.setage(s1,input("enter age"))

Student.setmarks(s1,input("enter marks"))


print("Name roll age", Student.display(s1))