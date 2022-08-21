lista=[2,5,6,4,7,3,78,6,12,51,25,34,26]

i=0
j=1

while j<len(lista):
    while i<j:
        if lista[i]<lista[j]:
            lista[j],lista[i]=lista[i],lista[j]
            i+=1
        else:
            i+=1
    j+=1
    i=0
            
print(lista)