# definition:
# Lambda is an anonymous one-time function
#Like a function, it can take a parameter and return a result

x = lambda a: a + 10
print(x(5))  # 15

# lambda - keyword
# a - arguments
# a + 10  - expresion
# expresion-a trqbva da e neshto koeto vrushta kraina stoinost.
# expresiona ne moje da e for cycle ili drugi neshta koito ne vrushtat kraina stoinost


# Lambda Example 1
x = lambda a, b: a * b
print(x(3, 4))  # 12
# Lambda Example 2
full_name = lambda first, last: f'I am {first} {last}'
result = full_name('Guido', 'van Rossum')
print(result)  # I am Guido van Rossum

