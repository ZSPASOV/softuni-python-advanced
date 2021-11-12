a = set([1, 2, 3, 4])
b = set([3, 4, 5, 6])
print(a.union(b))		  # Equivalent to a | b
print(a.intersection(b))  # Equivalent to a & b
print(a.issubset(b))      # Equivalent to a <= b
print(a.issuperset(b))           # Equivalent to a >= b
print(a.difference(b))          # Equivalent to a - b
print(a.symmetric_difference(b))  # Equivalent to a ^ b
