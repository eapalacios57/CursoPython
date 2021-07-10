print("VARIABLES LOCALES Y GLOBALES")
"""
variables local:se definin dentro de la funcion y no se pueden usar fuera de ella, solo estan disponibles dentro
A no ser que hagamos un return

variable globales:Son las que se declaran fuera de una funcion y estan disponibles dentro y fuera de ella
"""
#Variables Globales
frase = "Hola Mundo"
print(frase)

def holamundo():
    #frase = "Hola desde este nuevo mundo"
    print(frase)

holamundo()