__author__ = "Jose Luis Espiritu"
__date__ = "$24/02/2020 05:59:57 PM$"

import sqlite3

miConexion=sqlite3.connect("GestionProductos2")
miCursor=miConexion.cursor()

# LLAVE PRIMARIA Y LLAVE UNICA
#miCursor.execute('''
#    CREATE TABLE PRODUCTOS(
#    ID INTEGER PRIMARY KEY AUTOINCREMENT,
#    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#    PRECIO INTEGER,
#    SECCION  VARCHAR(20))
#''')

#productos=[
#    ("pelota",20,"jugueteria"),
#    ("pantalon",15,"confeccion"),
#    ("destronillador",25,"ferreteria"),
#    ("jarron",45,"ceramica"),
#    ("pantalones",35,"confeccion"),
#]
#
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

# READ
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")
productos=miCursor.fetchall()
print(productos)

# UPDATE
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

# DELETE
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miConexion.commit()

miConexion.close()