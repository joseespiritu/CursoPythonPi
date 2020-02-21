__author__ = "Jose Luis Espiritu"
__date__ = "$20/02/2020 06:54:50 PM$"

# LIBRERIAS PARA LA CREACION DE ARCHIVOS
from io import open

# MODO ESCRITURA, CREACION DE ARCHIVO DE TEXTO
#archivo_texto=open("archivo.txt","w")

# TEXTO EN EL ARCHIVO
#frase="Estupendo dia para aprender python \n el jueves"
#archivo_texto.write(frase)
#archivo_texto.close()

# MODO LECTURA, LEER LA INFORMACION DEL ARCHIVO
#archivo_texto=open("archivo.txt","r")
#texto=archivo_texto.read()
#archivo_texto.close()
#print(texto)

# ALMACENAR LA INFORMACION DEL ARCHIVO EN FORMA DE LISTA
#lineas_texto=archivo_texto.readlines()
#archivo_texto.close()
#print(lineas_texto[1])

# MODO AGREGAR, AGREGANDO INFORMACION AL ARCHIVO YA CREADO
archivo_texto=open("archivo.txt","a")
archivo_texto.write("\n siempre es una buena ocasion para estudiar Python")
archivo_texto.close()