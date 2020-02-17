# EXCEPCIONES PROPIAS
# SOLO SINTAXIS

def evaluaEdad(edad):
    if edad<0:
#        RAISE SOLO PERMITE ERRORES DEFINIDOS EN PYTHON
#        SE PUEDE ESPECIFICAR EL TIPO DE EXCEPCION
#        raise ZeroDivisionError("No se permiten edades negativas")
        raise TypeError("No se permiten edades negativas")
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "cuidate..."

edad_evaluada=evaluaEdad(-15)
try:
    print(edad_evaluada)
except TypeError as EdadIncorrecta:
    print("Edad incorrecta")

print("Programa finalizado")