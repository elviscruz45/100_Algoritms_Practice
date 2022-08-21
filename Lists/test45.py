# Python3 code to demonstrate working of
# Remove Consecutive K element records
# Using any() + list comprehension

# initializing list
test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 6

# Remove Consecutive K element records
# Using any() + list comprehension
res = [idx for idx in test_list if not any(idx[j] == K and idx[j + 1] == K for j in range(len(idx) - 1))]

# printing result
print("The records after removal : " + str(res))

