# ARCHIVO QUE DESCRIBE LA CONFIGURACION DEL PAQUETE DISTRIBUIBLE
# UNA VEZ CREADO EL ARCHIVO ES NECESARIO IR A LA CONSOLA
# MOVERSE A LA CARPETA DONDE SE CREO EL SETUP
# SE EJECUTA EL COMANDO python setup.py sdist
# EL ARCHIVO CREADO EN LA CARPETA DIST ES EL QUE SE DEBE DE COMPARTIR E INSTALAR
# PARA INSTALARLO DESDE LA CONSOLA SE VA A LA DIRECCION DONDE ESTA EL ARCHIVO COMPRIMIDO
# SE EJECUTA EL COMANDO pip3 install nombre_archivo
# Y AHORA SE PUEDEN IMPORTAR LAS FUNCIONES Y CLASES QUE SE HAYA CREADO EN ESE PAQUETE
# ESTE PAQUETE SE INSTALA PARA SU USO EN CUALQUIER SITIO
# PARA REMOVER EL ARCHIVO SE EJECUTA DESDE CUALQUIER DIRECTORIO EL COMANDO pip3 unistall nombre_paquete

from setuptools import setup

setup(
    name="paquete_calculos",
    version="1.0",
    description="Paquete de redondeo y potencia",
    author="Juan",
    author_email="jose@mail.com",
    url="www.jose.com",
    packages=["paquete_calculos","paquete_calculos.redondeo_potencia"]
    )