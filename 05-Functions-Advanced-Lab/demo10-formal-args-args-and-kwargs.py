# You can also use keyword arguments and *args
def some_func(arg1, *rest_args):
    print(arg1 + sum(rest_args))
some_func(5, 5, 10)   # 20
some_func(5) # 5
some_func() # Error
# The function above requires at least 1 argument

# So if you want to use all three of these in argument types then the order is
some_func(fargs, *args, **kwargs)
