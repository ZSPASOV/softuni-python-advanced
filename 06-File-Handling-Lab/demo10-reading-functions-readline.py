# Returns at most n bytes of a single line of a file
# It does not read more than one line
# If no argument is passed,  the entire line (or rest of the line) is read
file = open("text.txt")  # 'Hello, SoftUni!'
print(file.readline(5))  # 'Hello'
print(file.readline(5))  # ' ,Sof'
print(file.readline(5))  # 'tUni!'
print(file.readline())   # '' Goes to the new line
print(file.readline(5))  # 'Secon' Print second line
