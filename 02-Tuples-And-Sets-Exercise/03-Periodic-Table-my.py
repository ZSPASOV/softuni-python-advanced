n = int(input())
unique_elements = set()

for _ in range(n):
    elements = input().split()
    for i in elements:
        unique_elements.add(i)

print('\n'.join(unique_elements))