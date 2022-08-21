# Python3 code to demonstrate working of
# Random Matrix Element
# Using chain.from_iterables() + random.choice()
from itertools import chain
import random

# initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

# printing original list


# choice() for random number, from_iterables for flattening
res = list(chain.from_iterable(test_list))

# printing result
print(res)


