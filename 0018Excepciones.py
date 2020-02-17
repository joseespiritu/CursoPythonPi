def divide():
    
    try:
        op1=(float(input("Introduce el primer numero: ")))
        op2=(float(input("Introduce el segundo numero: ")))

        print("La division es: " + str(op1/op2))
        
#    EXCEPCION GENERAL
#    except:
#        print("Ha ocurrido un error")
    
#    EXCEPCIONES MULTIPLES
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No sepuede dividir entre 0!")
#    FINALLY SE EJECUTA PASE LO QUE PASE
#    FINALLY SOLO SE USA EN BASES DE DATOS PARA CERRAR LA CONEXION
    finally:
        print("Calculo finalizado")
    
divide()