#LISTAS
#SOPORTAN VARIOS TIPOS DE DATOS
miLista=["Maria", "Pepe", 5, "Maria", True, 78.35]

#FORMA CORRECTA DE IMPRIMIR UNA LISTA
print(miLista[:])

#IMPIMIR UN ELEMENTO DEL INDICE 2
print(miLista[2])

#CON INDICES NEGATIVOS LO CUENTA DESDE EL FINAL
#SOLO QUE NO EMPIEZA DESDE 0
print(miLista[-3])

#IMPIRIMIR DATOS DE LA LISTA CON RANGOS
#EXLUYE EL UTLIMO DATO
print(miLista[0:3])

#SIN EL PRIMER PARAMETRO USA POR DEFECTO EL 0
print(miLista[:3])
print(miLista[1:3])

#SIN EL SEGUNDO PARAMETRO VA DESDE EL PRIMERO QUE SE INDICA HASTA EL FINAL
print(miLista[2:])

#AGREGAR ELEMENTOS A UNA LISTA
miLista.append("Sandra")
print(miLista[:])

#AGREGAR UN ELEMENTO EN POSICION DESEADA
miLista.insert(2,"Luis")
print(miLista[:])

#AGREGAR VARIOS ELEMENTOS A UNA LISTA
miLista.extend(["Ana","Lucia"])
print(miLista[:])

#BUSCAR ELEMENTO POR INDICE, SI EL ELEMENTO SE REPITE SOLO DEVUELVE EL PRIMER ELEMENTO
print(miLista.index("Ana"))

#VERIFICAR SI UN ELEMENTO SE ENCUENTRA EN LA LISTA
print("Pepe" in miLista)

#REMOVER UN ELEMENTO DE LA LISTA
miLista.remove(5)
print(miLista[:])

#REMOVER EL ULTIMO ELEMENTO DE UNA LISTA
miLista.pop()
print(miLista[:])

#UNIENDO DOS LISTAS
miLista2=["Hola", "Lista"]
miLista3=miLista+miLista2
print(miLista3[:])

#REPETIR UNA LISTA
print(miLista2[:]*3)
