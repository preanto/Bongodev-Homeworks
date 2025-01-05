import math
class shape: 
    print("== Area & Perimeter Calculation ==")

class circle(shape):
    def __init__(self, r):
        self.r = r
    def calculate(self):
        print("The area of the circle is: ", 3.1416*self.r*self.r)
        print("The perimeter of the circle is: ", 2*3.1416*self.r)

class square(shape):
    def __init__(self, a):
        self.a = a
    def calculate(self):
        print("The area of the Square is: ", self.a*self.a)
        print("The perimeter of the Square is: ", self.a*4)
      
class triangle(shape):
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def calculate(self):
        s = (self.a+self.b+self.c)/2
        x = (s-self.a)*(s-self.b)*(s-self.c)*s
        area = math.sqrt(x)
        print("The area of the Triangle is: ", area)
        print("The perimeter of the Triangle is: ", self.a+self.b+self.c)

c1 = circle(3)
c1.calculate()
s1 = square(3)
s1.calculate()
t1 = triangle(8,3,9)
t1.calculate()