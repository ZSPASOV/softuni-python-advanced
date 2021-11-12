elements = input().split()
filtered = [x for x in elements if len(x) % 2 == 0]
print('\n'.join(filtered))