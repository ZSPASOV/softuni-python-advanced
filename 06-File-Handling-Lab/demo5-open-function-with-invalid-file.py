# If the file does not exist, FileNotFoundError is thrown
file = open('invalid.txt', 'r')  # FileNotFoundError
# It can be caught a try-finally block
try:
    file = open('invalid.txt', 'r')  # FileNotFoundError
except FileNotFoundError:
    print("File not found or path is incorrect")
finally:
    print("exit")
