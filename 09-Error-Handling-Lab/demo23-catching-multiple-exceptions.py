# Sometimes, you want to catch all errors that could possibly be generated, but usually you don't
# In most cases, you want to be as specific as possible

try:
    #some code
except ValueError:
    # handle the error
except TypeError:
    # handle the error