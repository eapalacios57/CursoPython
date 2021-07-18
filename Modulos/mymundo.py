def holamundo(nombre):
    return f"Hola Que tal estas{nombre}"

def calculadora(numero1, numero2, basicos=True):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    div = numero1 / numero2

    cadena = ""
    if basicos != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
    else:
        cadena += "\n"
        cadena += "Multiplicacion " + str(multi)
        cadena += "\n"
        cadena += "Div: " + str(div)

    return cadena