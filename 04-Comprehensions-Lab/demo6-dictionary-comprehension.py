# Creating a dictionary using dictionary comprehension

info = [("Peter", 22), ("Amy", 18), ("George", 35)]
dictionary = {key:value for (key, value) in info}
print(dictionary)
# {'Peter': 22, 'Amy': 18, 'George': 35}
# it can be done also the following way:
dictionary_2 = dict(info)
print(dictionary_2)
# {'Peter': 22, 'Amy': 18, 'George': 35}


# Form a dictionary with cube values of numbers
nums = [1, 2, 3]
cubes = {num:num ** 3 for num in nums}
print(cubes)
# {1: 1, 2: 8, 3: 27}


