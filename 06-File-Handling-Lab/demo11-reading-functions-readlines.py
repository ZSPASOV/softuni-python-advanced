# Read the remaining lines from the file object and returns them as a list
path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\text.txt'
file = open(path, 'r')
print(file.readlines()) # ['This is some random line\n', 'This is the second line\n', 'And this is the third one\n']

# Keep in mind every line in the file treats the new line symbol as a string
#file = open(path, 'r')
# this should be done to return the cursor at first position, otherwise it should be
# opened again
file.seek(0)
lines = file.readlines()
[print(line, end="") for line in lines]

