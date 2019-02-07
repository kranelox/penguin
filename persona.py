#Crear el archivo persona.py y el archivo dino.py dentro de la carpeta clases
#Crear una clase persona() que tenga como atributos nombre, edad y profesión. Al instanciar la clase tiene que saludar igual 
#que el dino, diciendo sus atributos.

class Persona:
    def __init__ (self, un_nombre, una_edad, una_prof):
        self.nombre = un_nombre 
        self.edad = una_edad
        self.profesion = una_prof
        print ("Hola soy", self.nombre, "tengo", self.edad, "anhos", "y soy una", self.profesion)
    
    def gritar(self, grito):#
        print("ESTOY GRITANDO!", grito)#

charlie = Persona("Shakira", 69, "cadera")
print(charlie.nombre)  #aca se imprime solo el nombre de la clase, porque ya le asignamos atributo a la clase entonces llamamos
#charlie.nombre para imprimir solo el valor del atributo "nombre".

charlie.gritar()

#Agregarle un atributo de clase a la clase persona que almacene una lista de hobbies
#Crear un metodo getter que retorne los hobbies de la persona
#Crear un metodo que agregue hobbies a la lista

class Person:
    hobbies = [] #lista vacia de hobbies
    def __init__ (self, name, hobbies):
        self.nombre = name
        self.hobbies = hobbies
        print("Hola, soy", self.nombre)

    def hobbies(self):
        return self.hobbies

    def mashobbies(self, nuevohobbie):
        self.hobbies.append(nuevohobbie) #append al atributo self.hobbies

churlito = Person("churlie", ["dormir", "comer"])