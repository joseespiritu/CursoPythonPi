__author__ = "Jose Luis Espiritu"
__date__ = "$27/02/2020 07:39:51 PM"

# VISUALIZAR COMENTARIOS EN TIEMPO DE EJECUCION

class Areas:
    
    """Esta clase calcula las areas de diferentes figuras geometricas"""
    
    def areaCuadrado(lado):

        """Calcula el area de un cuadrado
        elevando al cuadrado el lado pasado por parametro"""

        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):

        """Calcula el area de un triangulo utilizando los parametros base y altura"""

        return "El area del triangulo es: " + str((base*altura)/2)

# IMPRIMIR LA DOCUMENTACION CON PRINT
#print(areaCuadrado.__doc__)
#print(areaCuadrado(3))

# IMPRIMIR LA DOCUMENTACION CON EL METODO HELP
help(Areas.areaCuadrado)
help(Areas.areaTriangulo)

# IMPRIMIR AYUDA GENERAL EN LA CLASE
help(Areas)