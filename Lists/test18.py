# Python2 program to remove empty tuples
# from a list of tuples function to remove
# empty tuples using filter
def Remove(tuples):
	tuples = list(filter(lambda x:x!=(), tuples))
	return tuples

# Driver Code
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
print( Remove(tuples))

