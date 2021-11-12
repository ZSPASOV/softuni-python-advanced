# v1
import random as module_name

module_name.randint(1, 10)

# v2
from random import choice as gimme_one, shuffle as mix
gimme_one(["coke", "steak", "chips"])
mix(["coke", "steak", "chips"])

# v3 - importva vsichki, no ne e dobra praktika da se polzva

from math import *
sqrt(pi)

# v4

import random

print(random.choice([2,3,4]))
