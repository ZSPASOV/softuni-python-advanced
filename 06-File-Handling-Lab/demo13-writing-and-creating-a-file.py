# Writing and Creating a File
# Write, Append, Close Methods and with Statement
# Using 'w' (write) mode creates a file with the given name
# If the file exists, its overwritten
path = r'D:\Python Programming SoftUni Materials\03 Advanced\files for exercise\python.txt'
file = open(path, 'w')
file.write("This is the write command.\n")
file.write("It allows us to write in a particular file")
file.close()
