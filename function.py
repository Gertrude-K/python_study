#python functions
#  define the function using def keyword
#function cannot run until it is called by the name
#reusable block of code

def square_area():
    side=23
    area = side*side
    print(f"Area of square is: {area}")
square_area()

def triangle_area():
    base=10
    height=5
    area = 0.5*base*height
    print(f"Area of triangle is: {area}")
triangle_area()

def hello(name):
    print(f"Hello {name}")
hello("Alice")


#parameters -> variables that are passed to a function when it is called -INSIDE IT
#arguments -> values that are passed to a function when it is called - OUTSIDE IT

def triangle_area(base, height):
    area = 0.5*base*height
    return area

triangle1=triangle_area(10, 5)

def square_area(side):
    area = side*side
    return area

def circle_area(radius):
    area = 3.14*radius*radius
    return area
circle1=circle_area(7)

def rectangle_area(length, width):
    area = length*width
    return area

rectangle1=rectangle_area(10, 5)
rectangle2=rectangle_area(20, 10)