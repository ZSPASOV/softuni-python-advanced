from functools import reduce


def operate(op, *args):
    if op == '+':
        return reduce(lambda a, b: a + b, args)
    if op == '-':
        return reduce(lambda a, b: a - b, args)
    if op == '/':
        return reduce(lambda a, b: a / b, args)
    if op == '*':
        return reduce(lambda a, b: a * b, args)


print(operate('/', 2, 4, 1, 5, 3, 8))