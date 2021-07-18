cantantes = ['2pac', 'Antonio', 'Packer']
numeros = [1, 2, 4, 7, 5]

#Ordenar listas
print(numeros)
numeros.sort()
print(numeros)
#Anadir elmentos
cantantes.append("Natos y Waor")
cantantes.insert(4,"Enrique Iglesias")
print(cantantes)
#Elminar elmentos de una lista
cantantes.pop(1)
cantantes.remove('Packer')
print(cantantes)
#Dar la vuelta
numeros.reverse()
print(numeros)
#Contar numeros de elementos y buscar dentro de listas
print('2pac' in cantantes)

#Contar Elementos
print(cantantes)
print(len(cantantes))

#Cuantas veces aparece un elementos
print(numeros.count(7))

#Conseguir indice
print(cantantes.index("2pac"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)