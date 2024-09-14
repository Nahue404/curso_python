
num=int(input("Ingrese un numero o -99 para terminar:"))
array=[]
mayorprom=[]
suma=0
while num != -99:
    array.append(num)
    num=int(input("Ingrese un numero o -99 para terminar:"))

for i in array:
    suma += i

print("La suma de los elementos es:", suma)

tamano = len(array)

promedio = suma/tamano

print("El promedio de los numeros es:", int(promedio))

mayor=array[0]
menor=array[0]

for i in array:
    if mayor < i:
        mayor = i
    if menor > i:
        menor = i
    if promedio < i:
        mayorprom.append(i)

print("El numero mayor es:", mayor)
print("El numero menor es:", menor)
print(f"El numero mayor al promedio es:", {mayorprom})