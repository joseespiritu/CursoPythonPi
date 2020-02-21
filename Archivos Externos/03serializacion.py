__author__ = "Jose Luis Espiritu"
__date__ = "$20/02/2020 07:25:55 PM$"

import pickle

#lista_nombres=["Pedro","Ana","Maria","Isabel"]

# GUARDAR EL ARCHIVO EN FORMA BINARIA
#fichero_binario=open("lista_nombres","wb")

# VOLCADO DE LA LISTA AL ARCHIVO
#pickle.dump(lista_nombres,fichero_binario)

#fichero_binario.close()

# BORRANDO FICHERO DE LA MEMORIA
#del (fichero_binario)


# ABRIENDO FICHERO BINARIO
fichero=open("lista_nombres","rb")
lista=pickle.load(fichero)
print(lista)
