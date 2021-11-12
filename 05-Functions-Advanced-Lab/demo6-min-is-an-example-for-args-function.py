# min moje da vzima proizvolen broi positional arguments
print(min(1, 2, 3, 4, 5))

# nai veroqtno min funkciqta na backgrounda e implementirana po podoben nachin:

def min_our_version(*args):
    current_min = None
    for a in args:
        if current_min is None or a < current_min:
            current_min = a
        return current_min

print(min_our_version(1, 2, 3, 4, 5))