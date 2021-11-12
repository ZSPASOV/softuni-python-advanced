number_names = int(input())
list_of_names = []


for _ in range(number_names):
    name = input()
    list_of_names.append(name)

set_of_names = set(list_of_names)

for name in set_of_names:
    print(name)