#BUCLES
#NOTACION ESPECIAL CON PRINT

#UNIR TEXTOS CON VARIABLES
#EL SEGUNDO ARGUMENTO EN EL RANGE INDICA EL FIN
#EL TERCER ARGUMENTO EN EL RANGE INDICA EL CONTEO DESDE EL INCIIO HASTA EL FIN
#SOLO SE RECOMIENDA CUANDO EL FOR NECESITE VALORES NUMERICOS
for i in range(5,50,3):
    print(f"Valor de la variable {i}")

valido=False
email=input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido=True
    
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")