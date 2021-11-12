from collections import defaultdict

number_occurences = defaultdict(int)
numbers = map(float, input().split(' '))

for number in numbers:
    number_occurences[number] += 1

for number, occurece_count in number_occurences.items():
    print(f'{number} - {occurece_count} times')