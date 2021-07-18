import os

#Crear una carpeta

if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existi el directorio")

#Eliminar una carpeta
#os.rmdir('./mi_carpeta')

