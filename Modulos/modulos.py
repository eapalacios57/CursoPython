"""
Modulos:Son funcionalidaddes ya hechas para reutilizar.
"""
#Importar un modulo
#import mymundo
#Para importar solo una funcion
#from mymundo import holamundo
from mymundo import *

#print(mymundo.holamundo("Edgar Palacios"))
print(holamundo("Edgar Palacios"))
print(calculadora(3,5))
#Modulo fechas
import datetime
print(datetime.date.today())
fecha_completa= datetime.datetime.now()
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

#fecha_personalizada = fecha_completa.strptime("%d/%m/%Y, ")
#print("Mi fecha personalizada", fecha_personalizada)
print(datetime.datetime.now().timestamp())