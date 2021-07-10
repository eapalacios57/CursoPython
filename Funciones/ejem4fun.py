# Parametros Opcionales
print("PARAMETROS OPCIONALES")


def getEmpleado(nombre, id=None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")

    if id != None:
        print(f"id: {id}")


getEmpleado("Edgar Palacios", "123324354")
