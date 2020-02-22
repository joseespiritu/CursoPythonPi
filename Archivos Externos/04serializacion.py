__author__ = "Jose Luis Espiritu"
__date__ = "$21/02/2020 06:07:58 PM$"

import pickle

class Vehiculos():
    
    def __init__(self,marca,modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
    
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
            "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
            "\nFrenando: ", self.frena)
            
# SERIALIZACION DE OBJETOS
coche1=Vehiculos("Mazda","MX5")
coche2=Vehiculos("Seat","Leon")
coche3=Vehiculos("Renault","Megane")

coches=[coche1,coche2,coche3]

fichero=open("losCoches","wb")
pickle.dump(coches, fichero)
fichero.close()

del (fichero)

# LECTURA DEL FICHERO
ficheroApertura=open("losCoches","rb")
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()

for c in misCoches:
    print(c.estado())
