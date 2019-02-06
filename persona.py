#Crear el archivo persona.py y el archivo dino.py dentro de la carpeta clases
#Crear una clase persona() que tenga como atributos nombre, edad y profesión. Al instanciar la clase tiene que saludar igual 
#que el dino, diciendo sus atributos.

class Persona:
    def __init__ (self, un_nombre, una_edad, una_prof):
        self.nombre = un_nombre 
        self.edad = una_edad
        self.profesion = una_prof
        print ("Hola soy", self.nombre, "tengo", self.edad, "y soy un", self.profesion)

charlie = Persona("Charlie", 31, "Designer")
