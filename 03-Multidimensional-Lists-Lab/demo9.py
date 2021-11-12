matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# v1
for row in matrix:
    for value in row:
        print(value)

# v2

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])