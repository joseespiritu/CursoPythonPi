__author__ = "Jose Luis Espiritu"
__date__ = "$24/02/2020 05:45:23 PM$"

import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

# LLAVE PRIMARIA
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION  VARCHAR(20))
''')

productos=[
    ("pelota",20,"jugueteria"),
    ("pantalon",15,"confeccion"),
    ("destronillador",25,"ferreteria"),
    ("jarron",45,"ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()