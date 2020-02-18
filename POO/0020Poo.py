# PROGRAMACION ORIENTADA A OBJETOS

class Coche():
#    PROPIEDADES
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
#    METODOS
#    UN METODO ES UNA FUNCION QUE PERTENECE A UNA CLASE
    def arrancar(self):
        self.enmarcha=True
        
    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
# INSTANCIA DE CLASE
miCoche=Coche()

print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene: ",miCoche.ruedas," ruedas")
miCoche.arrancar()
print(miCoche.estado())