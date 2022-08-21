lista=[1, 2, 2, 3, 4, 5]

new=[lista[i] if lista[i]>lista[i+1] else lista[i+1] for i in range(len(lista)-1)] 
print(new)