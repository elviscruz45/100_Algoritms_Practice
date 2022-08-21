test_list = ["geekforgeeks", [5, 4, 3], "is", ["best", "good", "better"]]
K = 3
Output=[["geekforgeeks", 5, "is", "best"], 
        ["geekforgeeks", 4, "is", "good"],
        ["geekforgeeks", 3, "is", "better"]] 


"Inner elements picked and paired with similar indices. 5 -> “best”."


test_list = ["geekforgeeks", [5, 4], "is", ["best", "good"]]
K = 2
Output=[["geekforgeeks", 5, "is", "best"],
        ["geekforgeeks", 4, "is", "good"]] 
"Inner elements picked and paired with similar indices. 5 -> “best”. "

#--------------------------------------------------------------------------------------------------------
# Python3 code to demonstrate working of
# Optional Elements Combinations
# Using loop

# initializing list
test_list = ["geekforgeeks", [5, 4, 3, 4], "is",["best", "good", "better", "average"]]

# printing original list
print("The original list is : " + str(test_list))

# initializing size of inner Optional list
K = 4

res = []
cnt = 0
while cnt <= K - 1:
	temp = []
	
	# inner elements selections
	for idx in test_list:
		
		# checks for type of Elements
		if not isinstance(idx, list):
			temp.append(idx)
		else:
			temp.append(idx[cnt])
	cnt += 1
	res.append(temp)

# printing result
print("All index Combinations : " + str(res))

