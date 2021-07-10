"""
Solicitar la nota de 15 alumnos decide quien aprobo y reprobo
"""

contador = 1
aprobados = 0
repobaodos = 0
num_alumnos = int(input("¿Cuantos alumnos tienes?"))
while contador <= num_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno {contador}\"?"))
    
    if nota >= 5:
        aprobados += 1
    else:
        repobaodos +=1

    contador += 1
print(f"Alumonos aprobados: {aprobados}")
print(f"Alumnos Reprobados: {repobaodos}")