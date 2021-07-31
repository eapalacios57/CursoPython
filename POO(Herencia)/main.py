
#Herencia: Es la posibilidad de compartir atributos y metodos entre clases, Y que diferentes clases hereden de otras
import clases

persona = clases.Persona()
persona.setNombre("Edgar")
persona.setApellidos("Palacios")
persona.setAltura("170cm")
persona.setEdad("45 Años")

print(f"La personas es {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())
print("------------------------------------")

informatico = clases.Informatico()
informatico.setNombre("Jhon")
informatico.setApellidos("Palacios")


print(f"El informatico es: {informatico.getNombre()}{informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())