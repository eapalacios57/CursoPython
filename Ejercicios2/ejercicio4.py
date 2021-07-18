def comprobarTipado(dato, tipo):
    test = isinstance(dato,tipo)
    result = ""
    if test:
        print(f"Este dato es del tipo {type(dato)}")
    else:
        result = None
    return result


mi_lista= ["hola mundo", 77]
titulo = "Master en python"
numero = 1000
verdadero = True
print(comprobarTipado(mi_lista, list))
