import math
import exceptions


def find_circle_area(radius):
    if type(radius) not in [int, float]:
        raise exceptions.InvalidInputError(f'Radius cannot be of type {type(radius)}')
    return math.pi * (radius ** 2)



find_circle_area(True)
#     raise exceptions.InvalidInputError(f'Radius cannot be of type {type(radius)}')
# exceptions.InvalidInputError: Radius cannot be of type <class 'bool'>

# primer za prihvashtane na exception
try:
    print(find_circle_area(True))
except exceptions.InvalidInputError:
    print('Please enter valid input')