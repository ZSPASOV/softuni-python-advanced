# Using loops

matrix = []
for i in range(3):
    matrix.append([])
    for _ in range(2):
       matrix[i].append(0)
print(matrix)
# [
# [0, 0],
# [0, 0],
# [0, 0]
# ]

# Using comprehension
matrix = [[0 for i in range(2)] for i in range(3)]
print(matrix)
# [
# [0, 0],
# [0, 0],
# [0, 0]
# ]