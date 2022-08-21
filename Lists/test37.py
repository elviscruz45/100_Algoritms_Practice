test_list = ["geekforgeeks", [5, 4, 3, 4], "is", ["best", "good", "better", "average"]]

def lista(n):
    k=0
    for i in n:
        if isinstance(i,list):
            k=len(i)
    
    lista1=[]
    j=0
    while j<k:
        lista2=[]
        for i in n:
            if isinstance(i,list):
                lista2.append(i[j])
            else:
                lista2.append(i)
        lista1.append(lista2)
        j+=1
    return(lista1)
                
    

print(lista(test_list))