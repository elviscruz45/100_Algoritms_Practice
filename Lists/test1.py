"""
Given a list, write a Python program to swap first and last element of the list.

Examples: 

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]"""
#---------------------------------------------------------------------------------------------
# OPTION 1 Python3 program to swap first

def swap(n):
    key=n[len(n)-1]
    n[len(n)-1]=n[0]
    n[0]=key
    return n
    

print(swap([1, 2, 3]))

#----------------------------------------------------------------------------------------------------


# OPTION 2 Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	
	newList[0], newList[-1] = newList[-1], newList[0]

	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#---------------------------------------------------------------------------------------------

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	# Storing the first and last element
	# as a pair in a tuple variable get
	get = list[-1], list[0]
	
	# unpacking those elements
	list[0], list[-1] = get
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))

#---------------------------------------------------------------------------------------------
# Python3 program to illustrate
# the usage of * operarnd
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	start, *middle, end = list
	list = [end, *middle, start]
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

#---------------------------------------------------------------------------------------------
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	first = list.pop(0)
	last = list.pop(-1)
	
	list.insert(0, last)
	list.append(first)
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

