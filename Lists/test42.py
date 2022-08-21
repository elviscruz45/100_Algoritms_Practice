# Python 3 code to demonstrate
# the removal of all occurrences of
# a given item using filter() and __ne__

def remove_items(test_list, item):
	
	# using filter() + __ne__ to perform the task
	res = list(filter((item).__ne__, test_list))

	return res

# driver code
if __name__=="__main__":
	
	# initializing the list
	test_list = [1, 3, 4, 6, 5, 1]

	# the item which is to be removed
	item = 1

	# printing the original list
	print ("The original list is : " + str(test_list))

	# calling the function remove_items()
	res = remove_items(test_list, item)

	# printing result
	print ("The list after performing the remove operation is : " + str(res))

