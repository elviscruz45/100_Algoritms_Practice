# Python 3 code to demonstrate
# the removal of all occurrences of
# a given item using remove()

def remove_items(test_list, item):
	
    c = test_list.count(item)
    print(c)
    test_list.remove(item)
    test_list.remove(item)
    #for i in range(c):
    #    test_list.remove(item)

    return test_list

# driver code
if __name__=="__main__":
	test_list = [1, 3, 4, 6, 5, 1,1,1,13,5]
	item = 1
	res = remove_items(test_list, item)
	print (res)

