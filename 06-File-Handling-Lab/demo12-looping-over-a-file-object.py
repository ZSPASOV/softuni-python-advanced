# To return all lines from a file you can loop over it
# More memory efficient and fast manner
# Simple and easy to read
path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\text.txt'

file = open(path, 'r')

for line in file:
    print(line, end="")
    # print every line in a new line
