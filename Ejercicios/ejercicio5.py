"""
Muestren todos los numero entre numero que diga el usuario
"""
numero1 = int(input("Coloca el primer numero"))
numero2 = int(input("Conolcar el segundo numero"))

if numero1 < numero2:
    for contador in range(numero1, (numero2+1)):
        print(contador)
else:
    print("El primer numero debe ser mayor al segundo")