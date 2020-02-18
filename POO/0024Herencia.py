__author__ = "Jose Luis Espiritu"
__date__ = "$18/02/2020 12:28:08 PM$"

# CLASE PADRE
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

# CREANDO OTRA CLASE PADRE
class VElectricos():
    
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True

# HEREDANDO
class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
            
# HEREDANDO
class Moto(Vehiculos):
    hcaballito=""
    
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    
#    SOBREESCRIBIENDO EL METODO DE LA CLASE PADRE
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
            "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
            "\nFrenando: ", self.frena, "\n", self.hcaballito)


# INSTANCIA DE CLASES
miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

# HERENCIA MULTIPLE
# SE DA PREFERENCIA A LA PRIMER CLASE QUE SE HEREDA
class BicicletaEelectrica(VElectricos, Vehiculos):
    pass
#class BicicletaEelectrica(Vehiculos, VElectricos):
#    pass

miBici=BicicletaEelectrica()
    