import itertools


matrix = [
    [1, 3],
    [5, 7]
]

# * will pass each element of the matrix as a positional argument to the function
chained = itertools.chain(*matrix)

for e in chained:
    print(e)

total = sum(itertools.chain(*matrix))
print(total)