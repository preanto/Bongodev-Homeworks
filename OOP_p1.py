class circle:
    def __init__(self, a):
        self.a = a

    def perimeter(self):
        print("The perimeter of the circle is: ", 2*3.1416*self.a)

    def area(self):
        print("The area of the circle is: ", 3.1416*self.a*self.a)

circle1 = circle(3)
circle1.perimeter()
circle1.area()