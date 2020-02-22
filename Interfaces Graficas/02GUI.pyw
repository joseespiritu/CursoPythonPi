__author__ = "Jose Luis Espiritu"
__date__ = "$21/02/2020 07:04:22 PM$"

# IMPORTANDO LIBRERIA TKINTER
from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")
#raiz.resizable(1,0)
raiz.iconbitmap("user.ico")
#raiz.geometry("650x350")
raiz.config(bg="blue")

# EMPAQUETADO DE FRAME
miFrame=Frame()
#POSICION DEL FRAME
#miFrame.pack(fill="x")
miFrame.pack(fill="y", expand="True")
#miFrame.pack(side="left", anchor="n")
miFrame.config(bg="red")
miFrame.config(width="650", height="350")

#PROPIEDADES DEL BORDE
miFrame.config(bd=35)
#miFrame.config(relief="groove")
miFrame.config(relief="sunken")

# CAMBIAR CURSOR
#miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")

raiz.mainloop()