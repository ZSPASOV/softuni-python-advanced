# Using comprehension to traverse multidimensional lists
[print(num) for num in [j for j in matrix]]
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# It is bad practice to use comprehensions for multidimensional lists,
# since the code becomes messy and unreadable
