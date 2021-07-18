# Crear listas
numeros = [13, 8, 9, 11, 12, 9, 9, 10]
"""for numero in numeros:
    print(numero)"""

# Crear funcion recorrerla y devuelva string


def mostarlista(lista):
    resultado = ""

    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"

    return resultado


#print(mostarlista(numeros))
#Ordenar y mostarlista
numeros.sort()
print(mostarlista(numeros))

#Mostrar longitud
print(len(numeros))

#Busqueda en la lista
busqueda = int(input("Introduce el numero: "))

comprobar =  isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el numero: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"Buscar en la lista en el numero {busqueda}")
search = numeros.index(busqueda)
print(f"El numero buscado existe en la lista indice {search}")

