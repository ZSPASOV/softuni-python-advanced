# if a function calls itself infinite number of times it will go to maximum recursion
# depth exceeded error

def baba():
    return baba()

print(baba()) # RecursionError: maximum recursion depth exceeded
