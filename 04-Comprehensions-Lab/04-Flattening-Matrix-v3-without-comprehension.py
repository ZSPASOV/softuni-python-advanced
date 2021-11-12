# comprehension on one line - for comparison
# print([int(n) for _ in range(int(input())) for n in input().split(', ')])

# a version without comprehension
l = []
for _ in range(int(input())):
    for n in input().split(', '):
        l.append(int(n))
print(l)