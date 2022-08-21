from itertools import permutations

list_1 = ["a", "b", "c"]
list_2 = [1,4,9]
unique_combinations = []

permut=permutations(list_1,len(list_2))

for i in permut:
    zipped=zip(i,list_2)
    print(list(zipped))
    #unique_combinations.append(list(zipped))
    
    

