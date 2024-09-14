##Lista 2

array1=["futbol", "Pc", 18.6,18,[6,7,10.4],True,False, "Pc"]
array2=[200,250,"hola"]
array3=array1+array2

#Buscar valores dentro de un array
print("Pc" in array1)
#Saber el indice donde esta lo que busco
print(array1.index("Pc"))
#Cantidad de veces que tengo el valor en mi array
print(array1.count("Pc"))
#Borrar valores de un array
array1.remove("Pc")
print(array1)
#Limpiar
#array1.clear()
print(array1)
#Cambiar la posicion
array1.reverse()
print(array1)
#Ordenar de mayor a menor
array4=[1,2,8,-11,5]
array4.sort()
