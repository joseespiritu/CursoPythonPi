#NO EXISTE LA CONDICION SWITCH EN PYTHON
#PARA ESO EXISTEN EVALUACIONES MEJORADAS (ENCADENADAS)
edad=7

#PARA VALORES NEGATIVOS SE PUEDE APLICAR LO SIGUIENTE
if 0<edad<100:
	print("Edad correcta")
else:
	print("Edad incorrecta")

# EJEMPLO 2
salario_presidente=int(input("Introduce salario presidente: "))
# PARA CONCATENAR VALORES DIFERENTES
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Introduce salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Introduce salario jefe area: "))
print("Salario jefe area: " + str(salario_jefe_area))

salario_administrativo=int(input("Introduce salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")