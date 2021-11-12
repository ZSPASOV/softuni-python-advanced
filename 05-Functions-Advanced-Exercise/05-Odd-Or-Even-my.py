command = input()
list_numbers = [int(x) for x in input().split()]

if command == 'Odd':
    odd = list(filter(lambda x: x % 2 != 0, list_numbers))
    print(sum(odd) * len(list_numbers))
elif command == 'Even':
    even = list(filter(lambda x: x % 2 == 0, list_numbers))
    print(sum(even) * len(list_numbers))