# Set comprehensions are pretty similar to list comprehensions
# The only difference is that set comprehensions use curly brackets { }
nums = [1, 2, 3, 4, 4, 5, 6, 2, 1]
unique = {num for num in nums}
print(unique)
# {1, 2, 3, 4, 5, 6}
