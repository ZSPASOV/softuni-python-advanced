matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] += 1
print(matrix)
# [[2, 3, 4], [5, 6, 7], [8, 9 ,10]]
