n = int(input())
matrix = []

for row in range(n):
    line = list(input())
    matrix.append(line)

for row in matrix:
    print(''.join(row))