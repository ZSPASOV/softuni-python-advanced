# the check in set is faster than the check in a list, so we use set
# the difference in speed will be small, so a list can also be used instead
vowels = {'a', 'o', 'u', 'e', 'i', 'A', 'U', 'E', 'I', 'O'}
print(''.join([c for c in input() if c not in vowels]))