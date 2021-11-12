# We use *args to pack arguments into tuple

def some_func(*args):
    print(args)

some_func(1, 2, 3)           # (1, 2, 3)
some_func("peter", "george") # ("peter", "george")
some_func(True, False)       # (True, False)
some_func()                  # ()


