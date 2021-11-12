def baba(*args, **kwargs): # packing of args to tuple, packing of kwargs to dictionary.
    print(args)

baba(*[1, 2, 3], **{'a' : 1, 'b': 2}) # unpacking of args, unpacking kwargs



