# Tuple unpacking allows to extract tuple elements and assign them to elements
data = (1, 2, 3, 4, 5)
x, y, z, *other = data
print(x) # 1
print(y) # 2
print(z) # 3
print(other) # [4, 5]
