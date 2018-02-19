'''
Q2. Create a class Circle which has a class variable PI with value=22/7.
Make two methods getArea and getCircumference inside this Circle class.
Which when invoked returns area and circumference of each ciecle instances.
'''
class Circle:
    PI = 22/7
    def __init__(self,radius):
        self.radius = radius

    def getarea(self):
        area = (self.radius**2)*2*Circle.PI
        return area

    def getcircumference(self):
        circm = 2*self.radius*Circle.PI
        return circm


c1=Circle(int(input("enter the radius")))
print("The area is:",c1.getarea())
print("The circumference is:-", c1.getcircumference())