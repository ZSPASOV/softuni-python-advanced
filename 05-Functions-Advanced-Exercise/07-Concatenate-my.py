def concatenate(*args):
    empty_str = ''
    for i in args:
        empty_str += i
    return empty_str

print(concatenate("Soft", "Uni", "Is", "Great", "!"))