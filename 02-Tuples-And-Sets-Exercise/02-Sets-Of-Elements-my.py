n, m = [int(n) for n in (input().split())]
first_set = set()
second_set = set()


for _ in range(n):
    number = int(input())
    first_set.add(number)


for _ in range(m):
    number = int(input())
    second_set.add(number)

intersection = first_set & second_set

print('\n'.join({str(num) for num in intersection}))