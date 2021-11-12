# walrus operator is new in python 3.8
path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\text.txt'
f = open(path, 'rb')
while (c := f.read(1)) != b'':
    print(c)

c = 1 # statement: id does not return a value
f.read(1) != b'' # expresion:since it returns a value

c:= 2 # walrus operator - create expression, which assigns a value (still not supported in pycharm, use in command prompt)
