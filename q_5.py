'''
Define an employee class and initialize it with name and salary.
Now, make a classmethod that takes in a string parameter "name-2000" which creates an instance
and returns the instance based on parameter.
'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def getObjFromString(cls,inp):
        name,salary = inp.split("-")
        a = cls(name,salary)
        return a


e1 = Employee.getObjFromString(input("enter name-salary"))
e2 = Employee.getObjFromString(input("enter name-salary"))
print(e1.__dict__)
print(e2.__dict__)