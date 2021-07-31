class Persona:
    """
    nombre 
    apellidos
    altura
    edad
    """
    #METODODS
    def getNombre(self):
        return self.nombre
    
    def getApellidos(self):
        return self.apellidos
    
    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura
    
    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy Hablando"
    
    def caminar(self):
        return "Estoy Caminando"

    def dormir(self):
        return "Estoy Durmiendo"

class Informatico(Persona):
    """
    lenguajes
    experencia
    """
    def __init__(self):
        self.lenguajes = "HTML, CSS, JS, PHP"
        self.experencia = 5
    def getLenguajes(self):
        return self.lenguajes
    
    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    
    def programar(self):
        return "Estoy Programando"
    
    def repararPC(self):
        return "He reparado tu ordenador"