list_of_words = [word for word in input().split(', ')]
string_for_print = ''


for i in list_of_words:
    string_for_print += f'{i} -> {len(i)}, '

string_for_print = string_for_print[:-2]
print(string_for_print)