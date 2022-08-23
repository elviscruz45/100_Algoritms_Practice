comentario1="el precio de este producto es 15 soles"
comentario2="esta huevada, cuesta 25 soles, no me parece justo"



def extraer_numero(comentario):
    numeros="0123456789"
    dato=""
    for i in comentario:
        if i in numeros:
            dato+=i
    print(dato)
            
extraer_numero(comentario1)
extraer_numero(comentario2)