print("TABLAS DE MULTIPLICAR")
def tablas(numero):
    print(f"Tabla de Multiplicar del numero {numero}")

    for contador in range(11):
        operacion = numero*contador 
        print(f"{numero} * {contador} = {operacion}")
        print("\n")
tablas(2)
tablas(7)
tablas(100)

#Ejemplo 3.1
print("\n")
for num_tabla in range (1,11):
    tablas(num_tabla)