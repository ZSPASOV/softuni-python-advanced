from functools import reduce


def add(a, b):
    print(f'a = {a}')
    print(f'b = {b}')
    return a + b

# it calculates a cumulative sum
res = reduce(add, [1, 2, 3, 4, 5, 6])
print(f'res = {res}')

# using the positional argument 55 for an initial value of the cumulative sum
res = reduce(add, [1, 2, 3, 4, 5, 6], 55)
print(f'res = {res}')
