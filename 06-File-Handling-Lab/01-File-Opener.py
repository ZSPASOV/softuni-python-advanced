# You are given a file called text.txt with the following text:
# This is some random line
# This is the second line
# And this is the third one
# Create program that opens the file. If the file is found,
# print 'File found'. If the file is not found, print 'File not found'.
path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\text.txt'
try:
    open(path)
    print('File exists')
except FileNotFoundError:
    print('File not found')