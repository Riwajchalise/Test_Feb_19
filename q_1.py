"""
Q1. Create a SquareGeometry class which takes in length as initialize parameter. Make two methods getArea and getPerimeter inside this class.
Which when invoked returns area and perimeter of each square instance."""
class SquareGeometry:
    def __init__(self, length):
        self.length = length

    def getArea(self):
        a = self.length*self.length
        return a

    def getPerimeter(self):
        peremeter = self.length*4
        return peremeter

s1 = SquareGeometry(int(input("enter length of sq.")))

print(s1.getArea())
print(s1.getPerimeter())