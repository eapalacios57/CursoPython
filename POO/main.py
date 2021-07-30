#Programacion orienta a objetos
#Clase un Molde para crear diferentes objetos, atributos o metodos
#Definir un clase(Molde para crear mas objetos para ese tipo)
#(Coche) con caracteristicas similares

class Coche:

    #Atributos o propiedades(Variables)
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventadores"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Metodos(Son acciones que hace el objeto)(Funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def getEmpleado(self):
        return self.modelo


    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
#Fin definicion clase


##Crear Objetos /Instanciar la clase
coche = Coche()

coche.setColor("Amarillo")
coche.setModelo("Murcielago")
print(coche.marca, coche.getModelo(), coche.getColor())

#---------------///////////-----------------
#print(coche.marca, coche.color)
#print("Velocidad Actual ", coche.velocidad)
#coche.acelerar()
#coche.acelerar()
#coche.acelerar()
#coche.acelerar()
#coche.frenar()
#
#print("Velocidad Actual ", coche.velocidad)
#
#print("Velocidad Actual ", coche.getvelocidad())
#coche.acelerar()
#coche.acelerar()
#coche.acelerar()
#coche.acelerar()
#coche.frenar()
#
#print("Velocidad Actual ", coche.getvelocidad())
#
#CREAR MAS OBJETOS
print("-----------------------------------")
coche2 = Coche()
print(coche2.color)

