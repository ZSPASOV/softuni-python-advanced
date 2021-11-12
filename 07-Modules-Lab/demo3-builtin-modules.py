# The Python interpreter has a number of built-in modules
# They are pre-installed and we can call them at any given time
# In order to call them we use the keyword - import

import random
fruits = ["apple", "banana", "cherry"]

print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)
