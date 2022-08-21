# Python3 code to demonstrate working of
# Retain records with N occurrences of K
# Using count() + list comprehension

# initializing list
test_list = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# initializing N
N = 3

# Retain records with N occurrences of K
# Using count() + list comprehension
res = [ele for ele in test_list if ele.count(K) == N]

# printing result
print("Filtered tuples : " + str(res))

#----------------------------------------------------------------------------------------------

# Python3 code to demonstrate working of
# Retain records with N occurrences of K
# Using list comprehension + sum()

# initializing list
test_list = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# initializing N
N = 3

# Retain records with N occurrences of K
# Using list comprehension + sum()
res = [ele for ele in test_list if sum(cnt == K for cnt in ele) == N]

# printing result
print("Filtered tuples : " + str(res))

