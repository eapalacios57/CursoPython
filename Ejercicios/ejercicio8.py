"""
Hacer un programa que pida numero indefinidamente hasta merter 111
"""
contador = 1
while contador < 100:
    numero = int(input("Introduce un numero"))
    if numero == 111:
        break
    else:
        print(f"Has introducido el numero: {numero}")