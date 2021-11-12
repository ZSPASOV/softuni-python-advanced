def even_odd(*args):
    list = []
    if args[-1] == 'even':
        for i in range(len(args) - 1):
            if int(args[i]) % 2 == 0:
                list.append(int(args[i]))
    elif args[-1] == 'odd':
        for i in range(len(args) - 1):
            if int(args[i]) % 2 != 0:
                list.append(int(args[i]))
    return list

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))