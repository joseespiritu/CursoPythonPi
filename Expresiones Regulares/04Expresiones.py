__author__ = "Jose Luis Espiritu"
__date__ = "$27/02/2020 07:02:42 PM$"

import re

nombre1="Sandra Lopez"
nombre2="Antonio Gomez"
nombre3="Maria Lopez"
nombre4="Jara Lopez"
nombre5="Lara Lopez"
cadena1="546546546"
cadena2="a546546546"

# FUNCION MATCH SIN DISTINCION, BUSCA AL COMIENZO DEL TEXTO
if re.match("Sandra", nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")
   
     
# EL PUNTO INDICA UN CARACTER CUALQUIERA
if re.match(".ara", nombre4, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")
     
# VALORES QUE COMIENCEN CON NUMERO
if re.match("\d", cadena1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")
    
# FUNCION SEARCH, BUSCA EN TODA LA CADENA
if re.search("Lopez", nombre3, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")