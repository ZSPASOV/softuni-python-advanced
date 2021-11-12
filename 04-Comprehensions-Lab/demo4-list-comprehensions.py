# List Comprehensions provide an elegant way to create new lists
x = [num for num in range(5)]
# [0, 1, 2, 3, 4]

# List Comprehensions can include if-else statements
nums = [1, 2, 3, 4, 5, 6]
filtered = [True if x % 2 == 0 else False for x in nums]
# [False, True, False, True, False, True]
