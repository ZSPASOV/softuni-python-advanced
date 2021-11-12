# it is not a good practice, but it works

def add_and_multiply(a, b):
    add_result = a + b
    mul_result = a * b
    return add_result, mul_result

print((add_and_multiply(2, 3)))
add, mul = add_and_multiply(2, 3)
print(add)
print(mul)