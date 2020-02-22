# LABEL

from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miImagen=PhotoImage(file="python.png")
Label(miFrame, image=miImagen).place(x=10, y=10)

# ETIQUETA DENTRO DEL FRAME
#Label(miFrame, text="Hola GUI", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)


root.mainloop()