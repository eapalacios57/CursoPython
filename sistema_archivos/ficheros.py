from io import open
import pathlib
import shutil

#Abrir Archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")
#archivo = open(pathlib.path().absolute() + "fichero_texto.txt", "a+")
#Escribir dentro de un archivo
archivo.write("************* Soy un texto Metido desde python******************\n")

#Cerrar archivo
archivo.close()

#Abrir Archvio
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura= open(ruta, "r")

#Leer Contenido
#contenido = archivo_lectura.read()
#print(contenido)

#Leer Contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

#Copiar un archivo
"""
ruta_orignal = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
shutil.copyfile(ruta_orignal, ruta_nueva)
"""

#Mover archivo
"""
ruta_orignal = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiadonuevo.txt"
shutil.move(ruta_orignal, ruta_nueva)
"""
#Elminar Archvos
"""
import os
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiadonuevo.txt"
os.remove(ruta_nueva)
"""

#Comprabar si un archivo existe
import os.path

if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print("El archivo existe")
else:
    print("El archivo no existe")



