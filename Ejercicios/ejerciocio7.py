"""
Ejercicio mostrar todos los numero impares entre dos numero que decida el usuario
"""
numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce el segundo numero"))

if numero1 < numero2:
    for x in range(numero1, (numero2 + 1)):
        if x%2 == 0:
            print(f"{x} es par")
        else:
            print(f"{x} es IMPAR")
else:
    print("El numero 1 debe se mayor al 2")