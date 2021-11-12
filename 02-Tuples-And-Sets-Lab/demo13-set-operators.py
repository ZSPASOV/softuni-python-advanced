a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a | b) # Union -> {1, 2, 3, 4, 5, 6}
print(a & b) # Intersection -> {3, 4}
print(a < b) # Subset -> False
print(a - b) # Difference -> {1, 2}
print(b - a) # Difference -> {5, 6}
print(a ^ b) # Symmetric Difference -> {1, 2, 5, 6}
# Symmetric Difference written in different way, the same as above  -> {1, 2, 5, 6}
print((a - b) | (b-a))