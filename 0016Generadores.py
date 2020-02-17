# YIELD FROM
# ACCEDER A UN SUBELEMETO COMO LOS ARRAY DE DOS DIMENSIONES

# EL ASTERISCO INDICA QUE SE RECEBIRAN UN NUMERO INDETERMIDADO DE ELEMENTOS  EN FORMA DE TUPLA
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        
#        USANDO YIELD FROM
        yield from elemento
        
#        LA MANERA TRADICIONAL Y COMUN
#        for subElemento in elemento:
#            yield elemento
        

ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))