# GENERADORES
# SE CONSTRUYE UN OBJETO GENERADOR ITERABLE
# EN VEZ DE REGRESAR UN RETURN REGRESA UN YIELD
# EL PROGRAMA QUEDA EN STAND BY, SE DEVUELVEN LOS VALORES DE UNO EN UNO
# LA VENTAJA ES LA EFICIENCIA


# FUNCION
#def generaPares(limite):
#    num=1
#    miLista=[]
#    while num<limite:
#        miLista.append(num*2)
#        num=num+1
#    return miLista
#print(generaPares(10))

# GENERADOR
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1

devuelvePares=generaPares(10)

#DEVUELVE EL PRIMER VALOR QUE SE ENCUENTRA EN CADA LLAMADA
print(next(devuelvePares))

print("Aqui podria ir mas codigo")

print(next(devuelvePares))

print("Aqui podria ir mas codigo")

print(next(devuelvePares))