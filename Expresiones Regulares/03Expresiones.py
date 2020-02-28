__author__ = "Jose Luis Espiritu"
__date__ = "$27/02/2020 06:55:39 PM$"

import re

lista_nombres=['Ana',
                        'Pedro',
                        'Maria',
                        'Rosa',
                        'Sandra',
                        'Celia',
                        'Ma1',
                        'Se1',
                        'Ma2',
                        'Ba1',
                        'Ma3',
                        'Va1',
                        'Va2',
                        'Ma4',
                        'MaA',
                        'Ma5',
                        'MaB']
                        
# ELEMENTOS QUE SE ENCUENTRAN DESDE TAL LETRA HASTA TAL LETRA
for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento):
        print(elemento)
        
# TODOS LOS QUE ENCUENTRAN EN EL RANGO
for elemento in lista_nombres:
    if re.findall('Ma[0-3]', elemento):
        print(elemento)

# NEGACION DEL RANGO
for elemento in lista_nombres:
    if re.findall('Ma[^0-3]', elemento):
        print(elemento)

# ELEMENTOS DENTRO DEL RANGO
for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento)