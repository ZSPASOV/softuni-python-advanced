def list_manipulator(input_list, *args):
    working_list = input_list
    command, location, *others = args
    if command == 'remove':
        if location == 'end':
            if not others:
                working_list.pop()
            elif len(others) == 1:
                for _ in range(others[0]):
                    working_list.pop()
        if location == 'beginning':
            if not others:
                working_list.pop(0)
            elif len(others) == 1:
                for _ in range(others[0]):
                    working_list.pop(0)

    if command == 'add':
        if location == 'end':
            for i in others:
                working_list.append(i)
        if location == 'beginning':
            for i in sorted(others, reverse=True):
                working_list.insert(0, i)

    return working_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
