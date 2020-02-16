#CONDICIONALES CON OPERADORES LOGICOS
#AND, OR, IN
print("Programa de becas")
distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto: "))
print(salario_familiar)


#AL USAR EL OPERADOR AND SE DEBEN DE CUMPLIR TODAS LAS CONDICIONES
# AL USAR EL OPERADOR OR SE DEBEN DE CUMNPLR SOLO ALGUNA U OTRA
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")

#OPERADOR IN
#AQUI APLICA EL CASE SENSITIVE DEL INPUT
# USANDO LOWER AN UPPER
print("Asignaturas optativas")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)
else:
	print("La asignatura escogida no esta contemplada")