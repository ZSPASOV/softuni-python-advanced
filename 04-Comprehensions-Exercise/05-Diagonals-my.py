n = int(input())
matrix = [[int(number) for number in input().split(', ')] for _ in range(n)]


first_diagonal = [matrix[i][i] for i in range(n)]
second_diagonal = [matrix[i][n-i-1] for i in range(n)]
sum_first_diagonal = sum(matrix[i][i] for i in range(n))
sum_second_diagonal = sum(matrix[i][n-i-1] for i in range(n))

print(f'First diagonal: {", ".join([str(x) for x in first_diagonal])}. Sum: {sum_first_diagonal}')
print(f'Second diagonal: {", ".join([str(x) for x in second_diagonal])}. Sum: {sum_second_diagonal}')