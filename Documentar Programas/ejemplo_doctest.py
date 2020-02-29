__author__ = "Jose Luis Espiritu"
__date__ = "$28/02/2020 05:44:55 PM$"

import doctest

def area_triangulo(base, altura):
    
    """
    Calcula el area de un triangulo dado
    >>> area_triangulo(3,6)
    'El area del triangulo es: 9.0'
    
    >>> area_triangulo(4,5)
    'El area del triangulo es: 10.0'
    
    >>> area_triangulo(9,3)
    'El area del triangulo es: 13.5'
    """
    
    return "El area del triangulo es: "+ str((base*altura)/2)

def comprueba_mail(mail_usuario):
    """
    La funcion comprueba mail, evalua un mail recibido
    en busca de la @. Si tiene una @ es correcto
    si tiene mas de una @ es incorrecto
    si la @ esta al final es incorrecto
    
    >>> comprueba_mail('jose@cursos.com')
    True
    
    >>> comprueba_mail('josecursos.com@')
    False
    
    >>> comprueba_mail('josecursos.com')
    False
    
    >>> comprueba_mail('jose@cursos@.com')
    False
    
    """
    arroba=mail_usuario.count('@')
    if arroba!=1 or mail_usuario.rfind('@')==len(mail_usuario)-1 or mail_usuario.find('@')==0:
        return False
    else:
        return True
    
doctest.testmod()