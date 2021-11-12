# Note that the keys of the dictionary must match the names of the parameters of the function
# The order of the keys in the dictionary does not matter

def some_func(name, age):
    print(f"{name} is {age} years old")
person = {'age': 20, 'name': "Peter"}
some_func(**person) # Peter is 20 years old
