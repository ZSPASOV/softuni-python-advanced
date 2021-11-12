path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\numbers.txt'
print(sum([int(line.strip()) for line in  open(path, 'r')]))
