path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\numbers.txt'
file = open(path, 'r')
total = 0
for line in file:
    n = int(line.strip())
    total += n
print(total)