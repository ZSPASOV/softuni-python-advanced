command = input()
phone_book = {}
while command.isdigit() == False:
    args = command.split('-')
    name = args[0]
    phone = args[1]
    if name not in phone_book:
        phone_book[name] = ''
    phone_book[name] = phone
    command = input()

for _ in range(int(command)):
    search_name = input()
    if search_name in phone_book.keys():
        print(f'{search_name} -> {phone_book[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')

