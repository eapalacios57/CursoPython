# Añadir elementos a una lista
cantantes = list(('edwar', 'reikon', 'Reik'))
# Metodo append para agragar mas elementos a una lista
cantantes.append("Porta ")
cantantes.append("ALkilados")
print(cantantes)
# Recorer Lista con un for
print("******************Lsitados De Cantantes****************")
new_cantante = ""
while new_cantante != "parar":
    new_cantante = input("Introduce el nuevo cantante")
    if new_cantante != "parar":
        cantantes.append(new_cantante)

for cantante in cantantes:
    print(f"{cantantes.index(cantante)+1}. {cantante}")
