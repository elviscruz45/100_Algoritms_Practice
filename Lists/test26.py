test_casa= [[4, 1, 6], [7, 8], [4, 10, 8,20]]

for i in test_casa:
    j=0
    k=1
    while k<len(i):
        while j<k:
            if i[j]<i[k]:
                i[j],i[k]=i[k],i[j]
                j+=1
            else:
                j+=1
        k+=1
        j=0
        
print(test_casa)