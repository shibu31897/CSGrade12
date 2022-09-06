pi = 22/7
import math
def sub(a: int, b: int):
    if a > b:
        return a - b
    else:
        return b - a


def areaOfCircle(radius):
    """Area of triangle"""
    return math.ceil(pi*radius*radius)
