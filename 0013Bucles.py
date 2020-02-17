#BUCLES - BUCLE WHILE
#BUCLE INDETERMINADO
import math

i=1

while i<=10:
    print("Ejecucion " + str(i))
    i=i+1
    
print ("Termino la ejecucion")

edad=int(input("Introduce la edad: "))

while edad<5 or edad>100:
    print("Has introducido una edad incorrecta")
    edad=int(input("Introduce la edad: "))
    
print("Gracias por colaborar")
print("Edad del aspirante " + str(edad))

print("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")
    
    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;
   
    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))
        
