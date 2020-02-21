__author__ = "Jose Luis Espiritu"
__date__ = "$20/02/2020 07:06:53 PM$"

# PUNTEROS EN ARCHIVOS
from io import open

#archivo_texto=open("archivo.txt","r")

# MODO LECTURA Y ESCRITURA
archivo_texto=open("archivo.txt","r+")

#UNA VEZ QUE LEE EL ARCHIVO EL PUNTERO SE POSICIONA AL FINAL
#print(archivo_texto.read())

# METODO SEEK PARA POSICIONAR PUNTERO/CURSOR
# ESTE METODO MUESTRA DESDE LA POSICION QUE SE LE INDICA HASTA EL FIN DEL ARCHIVO
#archivo_texto.seek(0)
#print(archivo_texto.read())

# TAMBIEN SE PUEDE APLICAR EL METODO READ PARA POSICIONAR EL PUNTERO
# ESTE METODO SE DETIENE HASTA LA POSICION QUE SE HA INDICADO
#print(archivo_texto.read(11))
#print(archivo_texto.read())

# OBTENER LA MITAD DEL TEXTO DEL ARCHIVO
#archivo_texto.seek(len(archivo_texto.read())/2)
#print(archivo_texto.read())

# SI NO SE POSICIONA REESCRIBE LO QUE SE TIENE
#archivo_texto.write("Comienzo del texto")
lista_texto=archivo_texto.readlines()
lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()
