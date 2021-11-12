# Using loop
matrix = []
for i in range(3):
    matrix.append([])
    for j in range(1, 4):
       matrix[i].append(j)
print(matrix)
# [
# [1, 2, 3],
# [1, 2, 3],
# [1, 2, 3]
# ]

# Using comprehension
matrix = [[i for i in range(1, 4)] for j in range(3)]
print(matrix)
# [
# [1, 2, 3],
# [1, 2, 3],
# [1, 2, 3]
# ]