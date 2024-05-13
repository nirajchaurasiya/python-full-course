# Function Returning Multiple Values
# Problem: Create a function that returns
# both the area and circumference of a circle given its radius.

import math

PI = math.pi


def calculateAreaAndCircum(radius):
    area = PI * (radius**2)
    circumference = 2 * PI * radius

    return area, circumference


area, circumference = calculateAreaAndCircum(3)


print("Area: ", round(area, 2), "Circumference: ", round(circumference, 2))
