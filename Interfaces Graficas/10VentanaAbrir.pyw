__author__ = "Jose Luis Espiritu"
__date__ = "$22/02/2020 08:16:55 PM$"

from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"),
        ("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
#    DEVUELVE LA RUTA
    print(fichero)
    
Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()