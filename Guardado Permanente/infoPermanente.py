__author__ = "Jose Luis Espiritu"
__date__ = "$21/02/2020 06:20:35 PM$"

import pickle

class Persona:
    
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)
    
#    METODO STR PARA DEVOLVER LOS OBJETOS COMO TEXTO
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas:
    personas=[]
    
#    CONSTRUCTOR PARA CREAR FICHERO
    def __init__(self):
        listaDePersonas=open("ficheroExterno","ab+")
        listaDePersonas.seek(0)        
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
    
#    METODO PARA AGREGAR PERSONAS
    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
        
#    METODO PARA LEER PERSONAS
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
            
#            GUARDAR PERSONAS
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    
    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()
#persona=Persona("Sandra", "Femenino", 29)
#persona=Persona("Antonio", "Masculino", 49)
persona=Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(persona)
miLista.mostrarInfoFicheroExterno()
