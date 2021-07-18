#Capturarar excepciones y manejar errores en codigo
#Susceptible a fallas/errores
"""
try:
  nombre = input("¿Cual es tu nombre?")
  print(nombre)
  
  if len(nombre) > 1:
      nombre_usuario="El nombre es " + nombre
  print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("Todo a funcionado correctamente")
finally:
    print("Fin de la iteracion")
    """
#Multiples excepciones
"""
try:
    numero = int(input("Numero para elevarlo al cuadrado: "))
    print("El cuadrado es="+str(numero*numero))
except TypeError:
    print("Debes convertir tus cadenas en enteros en el codigo")
except ValueError:
    print("Introduce un numero correcto")
except Exception as e:
    print("Ha ocurrido un error", type(e).__name__)
"""

#Excepciones personalizadas
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))
    
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("No esta completo")
    else:
        print("Bienvenido al master en python")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)
