all = input().split(', ')
positive = [int(number) for number in all if int(number) >= 0]
negative = [number for number in all if int(number) < 0]
even = [number for number in all if int(number) % 2 == 0]
odd = [number for number in all if int(number) % 2 != 0]

# just for positive i show how to use comprehension in join
# to use join all elements of the list should be string
# for the other lists i do not convert to int at the rows above
print(f'Positive: {", ".join([str(x) for x in positive])}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')