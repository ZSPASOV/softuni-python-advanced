# Python has a set of built-in functions that we can call at any time
# List of some built-in functions
# abs()
# min()
# max()
# round()
# sum()
# filter()
# map()
# sorted()

# examples

print(abs(-42)) # 42
print(min([-1, 3, 5,])) # -1
print(min(-1, 3, 5)) # -1
print(max([-1, 3, 5])) # 5
print(max(-1, 3, 5)) # 5
print(round(4.2)) # 4
print(round(5.6)) # 6
print(sum([1, 2, 5])) # 8

print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))
print(sorted([56, 24, 100, 99]))
