n = int(input())
ascii_sum = 0
even_set= set()
odd_set = set()


for i in range(n):
    name = input()
    for j in name:
        ascii_sum += ord(j)
    quotient = int(ascii_sum / (i + 1))
    if quotient % 2 == 0:
        even_set.add(quotient)
    else:
        odd_set.add(quotient)
    ascii_sum = 0


sum_even = sum(even_set)
sum_odd = sum(odd_set)

even_set_str = {str(i) for i in even_set}
odd_set_str = {str(i) for i in odd_set}


if sum_odd == sum_even:
    print(', '.join(odd_set_str.union(even_set_str)))
elif sum_odd > sum_even:
    print(', '.join(odd_set_str.difference(even_set_str)))
else:
    print(', '.join(odd_set_str.symmetric_difference(even_set_str)))