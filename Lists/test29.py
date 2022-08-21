lista1=[[4, 5, 6], [2, 4, 5], [6, 7, 5]]
lista2= [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]


def lista(n,b):
    new=[]
    for i in lista1:
        lista3=[[i[0],i[b]]]
        lista4=[[i[1],i[b]]]
        lista5=lista3+lista4
        new.append(lista5)
    return new

print(lista(lista1,2))