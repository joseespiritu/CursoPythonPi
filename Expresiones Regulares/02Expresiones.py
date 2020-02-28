__author__ = "Jose Luis Espiritu"
__date__ = "$27/02/2020 06:43:45 PM$"

import re

lista_nombres=['Ana Gomez',
                        'Maria Martin',
                        'Sandra Lopez',
                        'Santiago Martin',
                        'Sandra Fernandez',
                        'camión',
                        'camion']

# ELEMENTOS QUE COMIENZAN POR
for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(elemento)
        
# ELEMENTOS QUE TERMINAN POR
for elemento in lista_nombres:
    if re.findall('Martin$', elemento):
        print(elemento)
        
# ELEMENTOS QUE CONTIENEN
for elemento in lista_nombres:
    if re.findall('[F]', elemento):
        print(elemento)
        
# ELEMENTOS QUE CONTIENEN
for elemento in lista_nombres:
    if re.findall('cami[oó]n', elemento):
        print(elemento)