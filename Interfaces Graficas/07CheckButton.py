__author__ = "Jose Luis Espiritu"
__date__ = "$22/02/2020 07:24:04 PM$"

from tkinter import *

raiz=Tk()
raiz.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""
    if playa.get()==1:
        opcionEscogida+=" playa"
    if montagna.get()==1:
        opcionEscogida+=" montana"
    if turismoRural.get()==1:
        opcionEscogida+=" Turismo Rural"    
    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="python.png", width=100, height=100)
Label(raiz, image=foto).pack()

frame=Frame(raiz)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montana", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

raiz.mainloop()