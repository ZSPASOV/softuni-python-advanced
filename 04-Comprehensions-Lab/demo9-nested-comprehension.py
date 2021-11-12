# Nested List Comprehensions are nothing but a list comprehension within another list comprehension
# It is quite similar to nested for loops
# Usually we use nested comprehensions when working with multidimensional lists (matrices)

# Creating a matrix with numbers

matrix = [[j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Flattening a matrix
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]

# flattening a matrix v2
import itertools
print(list(itertools.chain(*matrix)))

