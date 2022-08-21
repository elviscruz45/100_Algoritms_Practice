# python program to demonstrate
# unique combination of two lists
# using zip() and product() of itertools

# import itertools package
from itertools import product

# initialize lists
list_1 = ["b","c","d"]
list_2 = [1,4,9]

# create empty list to store the combinations
unique_combinations = []

# Extract Combination Mapping in two lists
# using zip() + product()
unique_combinations=list(
    list(zip(list_1, element))for element in product(list_2, repeat = len(list_1)))

# printing unique_combination list
print(unique_combinations)

