print("FUNCIONES PREDIFINIDAS")
nombre = "Edgar Palacios"

#Funciones generales
print(type(nombre))

#Detectar el tipado
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esta varibale es string")
else:
    print("No es una cadena")

#Limpiar espacios
frase = "  mi contenido  "
print(frase.strip())

#Eliminar variables
year = 2021
print(year)
del year


#Comprobar variable vacias
texto = " fff "
if len(texto) <= 0:
    print("Variable esta vacia", len(texto))
