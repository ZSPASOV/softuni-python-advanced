rows, cols = [int(n) for n in input().split()]
square_matrices = 0

matrix = []
for i in range(rows):
    row =  input().split(' ')
    matrix.append([])
    for j in range(cols):
       matrix[i].append(row[j])

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            square_matrices += 1
print(square_matrices)