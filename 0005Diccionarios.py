#Diccionarios
#clave:valor

midiccionario={"Alemania":"Berlin",23:"Jordan","Mosqueteros":3,"Francia":"Paris","Reino Unido":"Londres", "España":"Madrid"}

#ACCEDER A UN ELEMENTO POR CLAVE
print(midiccionario["España"])

#ACCEDER AL DICCIONARIO COMPLETO
print(midiccionario)

#AGREGAR UN ELEMENTO AL DICCIONARIO
midiccionario["Italia"]="Lisboa"
print(midiccionario)

#MODIFICAR EL VALOR DE UN DICCIONARIO
midiccionario["Italia"]="Roma"
print(midiccionario)

#ELIMINAR UN ELEMENTO DE UN DICCIONARIO
del midiccionario["Reino Unido"]
print(midiccionario)

#AÑADIENDO TUPLAS EN DICCIONARIOS
mitupla=["España","Francia", "Alemania"]
diccionario={mitupla[0]:"Madrid",mitupla[1]:"Paris", mitupla[2]:"Berlin"}
print(diccionario)

#ACCEDER A UN VALOR
print(diccionario["Francia"])

#TUPLA DENTRO DEL DICCIONARIO
diccionario2={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(diccionario2)

#DICCIONARIO DENTRO DE DICCIONARIO
diccionario3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(diccionario3["anillos"])

#METODOS PARA DICCIONARIOS

#IMPRIMIR LAS LLAVES
print(midiccionario.keys())

#IMPRIMRIR LOS VALORES
print(midiccionario.values())

#IMPRIMIR LA LONGITUD DEL DICCIONARIO
print(len(midiccionario))
