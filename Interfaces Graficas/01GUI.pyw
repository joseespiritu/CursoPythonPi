__author__ = "Jose Luis Espiritu"
__date__ = "$21/02/2020 06:49:00 PM$"

# STANDAR TKINTER LIBRARY
# IMPORTANDO LIBRERIA TKINTER
from tkinter import *

raiz=Tk()

#TITULO DE LA VENTANA
raiz.title("Ventana de pruebas")

# PERIMITIR REDIMENSION DE VENTANA (width true o false, height true o false)
raiz.resizable(1,1)

# CAMBIAR ICONO DE VENTANA
raiz.iconbitmap("user.ico")

# CAMBIAR TAMANIO POR DEFECTO DE LA VENTANA
raiz.geometry("650x350")

# CONFIGURACIONES DE LA VENTANA
raiz.config(bg="blue")

# METODO MAIN LOOP SIEMPRE AL FINAL
raiz.mainloop()