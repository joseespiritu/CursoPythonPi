__author__ = "Jose Luis Espiritu"
__date__ = "$24/02/2020 05:34:14 PM$"

# IMPORTAR LIBRERIA BASE DE DATOS
import sqlite3

# CREANDO Y HACENDO CONEXION A LA BASE DE DATOS
miConexion=sqlite3.connect("PrimeraBase")

# CREANDO CURSOR
miCursor=miConexion.cursor()

# EJECUTAR QUERY/CONSULTA
# CREATE
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

# INSERTAR UN REGISTRO
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

# INSERTAR VARIOS REGISTROS/PRODUCTOS
#variosProductos=[
#    ("Camiseta", 10, "Deportes"),
#    ("Jarron", 90, "Ceramica"),
#    ("Camion", 20, "Jugueteria")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

# VISUALIZAR DATOS
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()
print(variosProductos)
for producto in variosProductos:
    print("Nombre Articulo: ", producto[0], " Seccion: ", producto[2])

miConexion.commit()

# PARA VISUALIZAR EL CONTENIDO DE LA BASE DE DATOS SE NECESITA DB BROWSER
miConexion.close()