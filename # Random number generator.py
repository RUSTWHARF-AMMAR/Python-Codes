# Random number generator

import random
from string import digits

num_files = int(input("Select your Number range to choose from: "))
print(random.randrange(num_files))