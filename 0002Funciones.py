#FUNCIONES
#FUNCION SENCILLA SIN PARAMETROS
#def suma():
#    num1=5
#    num2=7
#    print(num1+num2)
    
#FUNCION SENCILLA CON PARAMETROS
def suma(num1,num2):
#    MANERA CORRECTA DE UTILIZAR LAS FUNCIONES
    resultado=num1+num2
    return resultado

#LLAMANDO FUNCION CON PARAMETROS
print(suma(5,7))
print(suma(2,3))
print(suma(35,358))

#GUARDANDO EL RESULTADO DE LA FUNCION
almacena_resultado=suma(5,8)
print(almacena_resultado)