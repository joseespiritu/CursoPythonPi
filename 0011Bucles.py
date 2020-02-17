#BUCLES
#RECORRER STRINGS
#TIPO RANGE SOLO APLICA PARA PYTHON 3

#ARGUMENTO END IMPRIME EL MENSAJE CON LO QUE SE ANIADA EN EL END
for i in [1, 2, 3]:
    print("Hola", end=" ")

#EJEMPLO ARROBA
contador=0
miEmail=input("Introduce tu direccion de email:  ")
for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1

if contador==2:
    print("El email es correcto")
else:
    print("El email es incorrecto")
    
#RANGE
#CREA UNA LISTA PARA RECORRERLA
for i in range(5):
    print(i)