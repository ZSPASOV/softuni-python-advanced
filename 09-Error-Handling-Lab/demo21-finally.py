try:
    int('1')
    print('end of try block')
    baba
except ValueError:
    print('sorry cannot cast that')
finally:
    print('always executed')