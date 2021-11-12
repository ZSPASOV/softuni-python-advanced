# Returns the first n bytes of the file
# Returns the entire file if number of bytes is not passed as an argument
file = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\asd.txt'
file = open(file)  # 'Hello, SoftUni!'
print(file.read(2))     # 'He'
print(file.read(2))     # 'll'
print(file.read(2))     # 'o,'
print(file.read())      # ' SoftUni!'
