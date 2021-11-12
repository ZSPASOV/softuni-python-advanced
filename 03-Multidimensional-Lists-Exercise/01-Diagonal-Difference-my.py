n = int(input())
primary_diagonal_sum = 0
secondary_diagonal_sum = 0


matrix = []
for i in range(n):
    row = list(map(lambda n: int(n), input().split(' ')))
    matrix.append([])
    for j in range(n):
       matrix[i].append(row[j])


sum_first_diagonal = sum(matrix[i][i] for i in range(n))
sum_second_diagonal = sum(matrix[i][n-i-1] for i in range(n))
difference = abs(sum_first_diagonal - sum_second_diagonal)
print(difference)