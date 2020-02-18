__author__ = "Jose Luis Espiritu"
__date__ = "$18/02/2020 11:46:43 AM$"

# PROGRAMACION ORIENTADA A OBJETOS
# ENCAPSULACION DE METODOS Y PROPIEDADES

class Coche():
#    PROPIEDADES
#    ESTADO INICIAL, CONSTRUCTOR
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
#    METODOS
#    UN METODO ES UNA FUNCION QUE PERTENECE A UNA CLASE
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
            
        else:
            return "El coche esta parado"
        
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ",
            self.__largoChasis)
            
#    METODO ENCAPSULADO
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina == "ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        
# INSTANCIAS DE CLASE
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()
# ACCEDIENDO AL METODO SIN ENCAPSULAR
#print(miCoche.chequeo_interno())

print("--------------A continuacion creamos el segundo objeto--------------")
miCoche2=Coche()
print(miCoche.arrancar(False))
miCoche2.estado()