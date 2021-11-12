# Using 'a' mode, open a file and write at the end of the file
# If the file is not exists, it's created
path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\python_two.txt'
file = open(path, 'a')
file.write("This is the write command.\n")
file.write("It allows us to write in a particular file")
file.close()

file = open(path, 'a')
lines = ["Write ", "in ", "file"]
file.writelines(lines)  # Write multiple strings
file.close()
