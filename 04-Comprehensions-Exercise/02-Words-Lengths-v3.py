elements = input().split(', ')
result = [f'{x} -> {len(x)}' for x in elements]
print(', '.join(result))
