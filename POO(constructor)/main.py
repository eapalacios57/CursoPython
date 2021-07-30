from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Negro", "Toyota", "Citron", 100, 180, 6)

print(carro.getInfo())
print(carro1.getInfo())

#Dectetar Tipado
if type(carro) == Coche:
    print("--Es un objeto correcto--")
else:
    print("---No es un objeto---")

#Visibilidad de nuestros atributos
print(carro.soy_publico)
print(carro.getPrivado())
