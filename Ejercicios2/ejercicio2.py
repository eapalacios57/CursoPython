  #Escribir un programa que añada valores a una lista mientras sul longitud sea menor a 120 y luego mostar la lista

coleccion = []
"""for contador in range(0, 120):
    coleccion.append(f"elementos: {contador}")
    print("Mostrando el:" + coleccion[contador])
print(coleccion)"""
contador = 0
while contador < 120:
    coleccion.append(f"elementos: {contador}")
    print("Mostrando el:" + coleccion[contador])
    contador +=1
print(coleccion)