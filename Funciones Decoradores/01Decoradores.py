__author__ = "Jose Luis Espiritu"
__date__ = "$27/02/2020 07:15:54 PM$"

# ANIADEN FUNCIONALIDADES A OTRAS FUNCIONES, DEVUELVE UNA FUNCION

def funcion_decoradora(funcion_parametro):
    def funcion_interior():
#         ACCIONES ADICIONALES QUE DECORAN
        print("Vamos a realizar un calculo: ")
        
        funcion_parametro()
        
#         ACCIONES ADICIONALES QUE DECORAN
        print("Hemos terminado el calculo")
    
    return funcion_interior
    
@funcion_decoradora
def suma():
    print(15 + 20)
    
@funcion_decoradora   
def resta():
    print(30-10)

suma()
resta()