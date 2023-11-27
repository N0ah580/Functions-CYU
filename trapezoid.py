# Programmer: Noah
# Description: Trapezoid

from math import pi

def get_trapezoid_area (base, top, height):
    #convert to float
    base = float(base)
    top = float(top)
    height = float(height)
    #calculate the area of the trapezoid
    num1 = base + top/2
    answer = num1 * height
    return answer


