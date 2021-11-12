import itertools

rows, cols = [int(element) for element in input().split(', ')]
matrix = [[int(number) for number in input().split(', ')] for _ in range(rows)]
total = sum(itertools.chain(*matrix))
# passing argument as * makes it positional arguments
# it is identical to:
# total = 0
# for row in matrix:
#     total += sum(row)

print(total)
print(matrix)