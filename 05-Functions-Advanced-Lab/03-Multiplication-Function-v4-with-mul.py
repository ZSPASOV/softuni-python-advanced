from operator import mul
from functools import reduce

def multiply(*args):
    return reduce(mul, args)

