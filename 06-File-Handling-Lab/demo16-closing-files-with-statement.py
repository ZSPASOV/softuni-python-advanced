# Files opened with with statement will be closed automatically once it leaves the with block
# Provide much cleaner syntax and exceptions handling
path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\file.txt'
with open(path, "w") as f:
    f.write("Hello World!!!")
