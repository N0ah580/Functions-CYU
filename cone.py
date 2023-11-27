# Programmer: Noah
# Description: Cone

from math import hypot
from math import pi


def get_volume (radius, height):
    step_1 = pi * radius ** 2 * height
    answer = step_1 / 3
    return (f"{answer}")

def get_surface_area (radius, height):
    part_1 = pi * radius ** 2
    slant = hypot (radius, height)
    part_2 = pi * radius * slant
    answer_sa = part_1 + part_2
    return (f"{answer_sa}ge")