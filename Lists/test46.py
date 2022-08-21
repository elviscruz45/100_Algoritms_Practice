# Python3 code to demonstrate
# Replace index elements with elements in Other List
# using list comprehension

# Initializing lists
test_list1 = ['Gfg', 'is', 'best']
test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Replace index elements with elements in Other List
# using list comprehension
res = [test_list1[idx] for idx in test_list2]
			
# printing result
print ("The lists after index elements replacements is : " + str(res))

