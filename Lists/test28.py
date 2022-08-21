lista=[2,5,6,4,7,3,78,6,12,51,25,34,26]
 

for j in range(1,len(lista)):
    key=lista[j]
    i=j-1
    while i>0 and lista[i]>key:
        lista[i+1]=lista[i]
        i=i-1
    lista[i+1]=key

print(lista)