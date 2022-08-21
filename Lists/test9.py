def sum_digit(n):
    listas=[]
    for i in n:
        hola=list(str(i))
        num=0
        for dig in hola:
            num+=int(dig)
        listas.append(num)
    
    return listas
    

n = [12, 67, 98, 34]


#--------------------------------------------------------------------------------------------------------

# Python3 code to demonstrate
# Sum of number digits in List
# using sum() + list comprehension

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using sum() + list comprehension
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))

# printing result
print ("List Integer Summation : " + str(res))

#--------------------------------------------------------------------------------------------------------
# Python3 code to demonstrate
# Sum of number digits in a List
# using sum() + reduce()
from functools import reduce

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List
# using sum() + reduce()
res = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in test_list]

# printing result
print("List Integer Summation : " + str(res))

