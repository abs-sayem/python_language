# Write a Python program which accepts the radius of a circle from the user and compute the area.
# Area of a circle: (pi*radius^2). [pi is a constant, so we only need the value of radius

from math import pi
radius = float(input("Enter the radius of the circle: "))
def area_of_circle(r):
    return (pi*(r*r))   # or try this: (pi*r**2)

print("Area of the Circle:", area_of_circle(radius))