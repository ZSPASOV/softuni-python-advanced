list_of_words = [word for word in input().split(', ')]
string_for_print = ''


for i in list_of_words:
    if i == list_of_words[-1]:
        string_for_print += f'{i} -> {len(i)}'
    elif i != list_of_words[-1]:
        string_for_print += f'{i} -> {len(i)}, '


print(string_for_print)