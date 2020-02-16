#CONDICIONALES IF

print("Programa de evaluación de notas de alumnos")

#INTRODUCIR VALOR POR TECLADO, TODOS LOS VALORES INGRESADOS SON CONSIDERADOS STRINGS
nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
		#SI SE DECLARA UNA VARIABLE DENTRO DE ESTE IF, SOLO FUNCIONA PARA EL IF
		#ESTO SE CONOCE COMO AMBITO
	return valoracion

#TRANSFORMANDO STRING A INT
print(evaluacion(int(nota_alumno)))