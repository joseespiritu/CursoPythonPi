# BUCLES
# CONTINUE, PASS Y ELSE

for letra in "Python":
#    CONTINUE IGNORA LO QUE SIGUE SI ESA CONDICION SE CUMPLE
    if letra=="h":
        continue
    print("Viendo la letra: " + letra)
    
# DEVOLDIENDO EL NUMERO DE LETRAS
# IGNORANDO EL ESPACIO EN BLANCO
contador=0
texto="Python is great"
for i in texto:
    if i==" ":
        continue
    contador+=1
print(contador)

# EN ESTE CASO PASS SE UTILIZA PARA
#while True:
#    pass
#
#class MiClase:
#    pass # Para implementar mas tarde

# ELSE CON FOR
# PUEDE SER UNA ALTERNATIVA PARA EL WHILE
email=input("Introduce tu email: ")
for i in email:
    if i == "@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)