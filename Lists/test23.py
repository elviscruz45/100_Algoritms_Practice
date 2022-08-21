st_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]

ll=[]

for i in st_list1:
    if i not in test_list2:
        ll.append(i)
for i in test_list2:
    if i not in st_list1:
        ll.append(i)

#--------------------------------------------------------------------------------------------------------

set1=set(map(tuple,st_list1)) ^ (set(map(tuple,test_list2)))

print(set1)
