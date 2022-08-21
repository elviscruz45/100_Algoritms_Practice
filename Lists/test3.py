
"""Sometimes, while working with data records we 
can have a problem in which we need to perform certain 
swap operation in which we need to change one element with other over entire string list.
This has application in both day-day and data Science domain. Lets discuss certain ways
in which this task can be performed."""

# Python3 code to demonstrate
# Swap elements in String list
# using replace() + list comprehension

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]

# printing result
print ("List after performing character swaps : " + str(res))

#-------------------------------------------------------------------------------------------------------------

# Python3 code to demonstrate
# Swap elements in String list
# using replace() + join() + split()

# Initializing list
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# printing original lists
print("The original list is : " + str(test_list))

# Swap elements in String list
# using replace() + join() + split()
res = ", ".join(test_list)
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')

# printing result
print ("List after performing character swaps : " + str(res))

