# ALGUNOS METODOS PARA CADENAS
nombreUsuario=input("Introduce tu nombre de usuario: ")
print("El nombre es: ", nombreUsuario)

#PASAR A MAYUSCULAS
print("El nombre es: ", nombreUsuario.upper())

#PASAR A MINUSCULAS
print("El nombre es: ", nombreUsuario.lower())

#LA PRIMERA LETRA EN MAYUSCULAS
print("El nombre es: ", nombreUsuario.capitalize())

edad=input("Introduce la edad: ")
while(edad.isdigit() == False):
    print("Por favor introduce un valor numerico")
    edad=input("Introduce la edad: ")
    
print(edad.isdigit())
if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")
