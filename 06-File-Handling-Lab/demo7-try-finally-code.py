# just a demo

l = [1, 2, 3]

try:
    print(l[100])
except IndexError:
    print('No such index')
# vinagi stiga do finally blocka
finally:
    print('the final stuff')