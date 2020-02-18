__author__ = "Jose Luis Espiritu"
__date__ = "$18/02/2020 12:53:15 PM$"

# POO, HERENCIA, SUPER, ISINSTANCE

class Persona():
    
    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia
    
    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario, "Antiguedad: ",self.antiguedad)

Manuel=Empleado(1500,15, "Manuel", 55, "Colombia")
Antonio=Persona("Manuel", 55, "Colombia")
Manuel.descripcion()

# VERIFICANDO SI ES UNA INSTANCIA DE UNA CLASE
print(isinstance(Manuel,Empleado))
print(isinstance(Manuel,Persona))
print(isinstance(Antonio,Empleado))
print(isinstance(Antonio,Persona))