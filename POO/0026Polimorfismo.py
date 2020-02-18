__author__ = "Jose Luis Espiritu"
__date__ = "$18/02/2020 01:21:13 PM$"

# POLIMORFISMO
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class Camion(): 
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)