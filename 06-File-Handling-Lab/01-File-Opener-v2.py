# You are given a file called text.txt with the following text:
# This is some random line
# This is the second line
# And this is the third one
# Create program that opens the file. If the file is found,
# print 'File found'. If the file is not found, print 'File not found'.
file = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\text.txt'
import os.path
print('File exists' if os.path.exists(file) else 'File not found')