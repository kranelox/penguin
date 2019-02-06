#Crear el archivo persona.py y el archivo dino.py dentro de la carpeta clases
#Crear una clase persona() que tenga como atributos nombre, edad y profesión. Al instanciar la clase tiene que saludar igual 
#que el dino, diciendo sus atributos.

class Persona:
    def __init__ (self, un_nombre, una_edad, una_prof):
        self.nombre = un_nombre 
        self.edad = una_edad
        self.profesion = una_prof
        print ("Hola soy", self.nombre, "tengo", self.edad, "anhos", "y soy una", self.profesion)
    
    def gritar(self):
        print("ESTOY GRITANDO!", self.profesion)

charlie = Persona("Shakira", 69, "cadera")
print(charlie.nombre)  #aca se imprime solo el nombre de la clase, porque ya le asignamos atributo a la clase entonces llamamos
#charlie.nombre para imprimir solo el valor del atributo "nombre".

charlie.gritar()