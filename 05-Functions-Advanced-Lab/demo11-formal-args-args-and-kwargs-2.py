def baba(a, *args, **kwargs):
    print(args)
    print(kwargs)

baba(1)
# ()
# {}

# in the example above:
# the value of *args in that example will be an empty tuple
# the value of **kwargs in that example will be an empty dictionary

baba(1, 2, c=5)

# (2,)
# {'c': 5}

