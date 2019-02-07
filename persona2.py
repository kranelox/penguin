class Person:
    hobbies = [] #lista vacia de hobbies
    def __init__ (self, name, hobbies):
        self.nombre = name
        self.hobbies = hobbies
        print("Hola, soy", self.nombre)

    def hobbies2(self):
        return self.hobbies

    def mashobbies(self, nuevohobbie):
        self.hobbies.append(nuevohobbie) #append al atributo self.hobbies

churlito = Person("churlie", ["dormir", "comer"])