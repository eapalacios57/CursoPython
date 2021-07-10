from typing import Text


print("EJERCICIO 6 FUNCIONES DENTRO DE OTRAS")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"El apellido es: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto 

print(devuelveTodo("Edgar", "Palacios"))
