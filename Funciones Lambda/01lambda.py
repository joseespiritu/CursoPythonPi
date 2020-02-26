__author__ = "Jose Luis Espiritu"
__date__ = "$25/02/2020 07:53:27 PM$"

# EJEMPLO FUNCIONES/ EXPRESIONES LAMBDA
# SIMPLIFICAN LA SINTAXIS DE FUNCIONES SIMPLES

# REALIZAR REPETIDAMENTE EL AREA DE UN TRIANGULO
#def area_triangulo(base, altura):
#    return (base*altura)/2
#
#triangulo1=area_triangulo(5, 7)
#triangulo2=area_triangulo(8, 6)
#
#print(triangulo1)
#print(triangulo2)

area_triangulo=lambda base,altura:(base*altura)/2

print(area_triangulo(7,5))
print(area_triangulo(9,6))

#al_cubo=lambda numero:pow(numero, 3)
al_cubo=lambda numero:numero**3

print(al_cubo(13))

destacar_valor=lambda comision:"{} $".format(comision)
comision_Ana=15585
print(destacar_valor(comision_Ana))