# Function Calling Itself

# The process in which a function calls itself is called recursion
# The function that is calling itself is called a recursive function
# A recursive function has the following structure
# A base case
# A recursive case

# Base Case and Recursive Case
# The base case in a recursion returns a value without making any other recursive calls
# It is the condition for the recursion to stop
# The recursive case is the central part of the recursive function
# It is the solution to the bigger problem expressed in terms of smaller problems

# example
# Factorial recursive representation
def fact(n):
   if n == 1: # base case
      return 1
   return n * fact(n - 1) # recursive case
