# Programmer: Noah
# Description: Trapezoid

from math import pi

def get_trapezoid_area (base, top, height):
    
    #calculate the area of the trapezoid
    num1 = base + top
    num2 = num1 / 2
    answer = num2 * height
    return answer


