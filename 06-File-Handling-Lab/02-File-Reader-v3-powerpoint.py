# Create a program that reads the numbers from the file called 'numbers.txt'
# Print on the console the sum of those numbers
numbers_file = open('numbers.txt', 'r')
numbers_sum = 0
for number in numbers_file:
    numbers_sum += int(number)
print(numbers_sum)
