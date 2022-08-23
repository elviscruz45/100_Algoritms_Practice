text1= "geeks quiz practice code"
text2 = "my name is laxmi"

def reverse(text):
    lista=list(text.split(" "))
    reverso=[lista[len(lista)-1-i] for i in range(len(lista))]
    return " ".join(reverso)

print(reverse(text1))


print(reverse(text2))