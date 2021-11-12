n = [1, 2, 3, 4, 5]
filtered = [
    'baba' if x % 2 == 0 else 'dqdo' # output expression
    for x in n                       # iteration over n
    if x % 2 == 0                    # filtration
]

print(filtered)