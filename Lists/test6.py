#Python | Cloning or Copying a list

# Python code to clone or copy a list
# Using list comprehension
def Cloning(li1):
	li_copy = [i for i in li1]
	return li_copy

# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

#--------------------------------------------------------------------------------------------------------

# importing copy module
import copy

# initializing list 1
lis1 = [1, 2, [3,5], 4]

# using copy for shallow copy
lis2 = copy.copy(li1)

lis1[0]=100
print(lis1)
print(lis2)

