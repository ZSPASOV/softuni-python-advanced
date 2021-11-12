# Create program that opens the file called 'text.txt'
# If the file is found, print 'File found'
# If the file is not found, print 'File not found'
try:
    text_file = open('text.txt', 'r')
    print("File found")
except FileNotFoundError:
    print("File not found")
