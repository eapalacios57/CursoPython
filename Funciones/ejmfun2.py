"""nombre = "Edgar Palaciosa"
def mostrarNombre(nombre):
    print(f"Tu nombre es: {nombre}")
mostrarNombre("Edgar Palacios")
mostrarNombre("Paquito")
mostrarNombre("Juanfran")"""
def mostrarNombre(nombre, edad):
    print(f"tu nombre es {nombre}")

    if edad >= 18:
        print("Eres mayor de edad")

nombre = input("Introduce tu nombre")
edad = int(input("Introduce tu edad"))
mostrarNombre(nombre, edad)