__author__ = "Jose Luis Espiritu"
__date__ = "$27/02/2020 06:32:24 PM$"

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje con estructura sencilla"

print(re.search("aprender", cadena))
print(re.search("aprenderrrr", cadena))

textoBuscar="Python"

#if re.search(textoBuscar, cadena) is not None:
#    print("He encontrado el texto")
#else:
#    print("No he encontrado el texto")

textoEncontrado=re.search(textoBuscar, cadena)

# NUMERO DE CARACTER DONDE COMIENZA A ENCONTRAR EL TEXTO
print(textoEncontrado.start())

# NUMERO DE CARACTER DONDE FINALIZA EL TEXTO
print(textoEncontrado.end())

# DEVUELVE UNA TUPLA CON EL INICIO Y EL FIN
print(textoEncontrado.span())

# DEVUELVE TODO LO QUE COINCIDE CON EL TEXTO BUSCADO
print(re.findall(textoBuscar,cadena))

print(len(re.findall(textoBuscar,cadena)))
