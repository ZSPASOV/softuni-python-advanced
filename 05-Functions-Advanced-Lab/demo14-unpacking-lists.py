# Note that the length of the list that you unpack must be the same
# as the number of parameters in the function
def print_nums(a, b, c):
    print(a, b, c)
nums = [1, 2, 3]
print_nums(*nums)   # 1 2 3

def baba(*args): # packing of args to tuple
    print(args)

baba(*[1, 2, 3]) # unpacking of args


