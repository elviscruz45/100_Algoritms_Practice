test_list = ["Gfg", 113, "is", 8, "Best", 10, "for", 18, "Geeks", 13]
key_list = ["name" , "id"]
new=[]

for i in range(0,len(test_list),2):
    a={key_list[0]:test_list[i],key_list[1]:test_list[i+1]}
    new.append(a)
    
#--------------------------------------------------------------------------------------------------------


lista=[{key_list[0]:test_list[i],key_list[1]:test_list[i+1]} for i in range(0,len(test_list),2)]

print(lista)