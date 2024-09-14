#cadena = ""

#cadena = input("¿Como se llama tu proyecto?\n")
#print(f"El nombre es",{cadena})

#cadena = int(input("¿Que version es?\n"))
#print(f"Tu proyecto se llama: {cadena+1}")

#app="python"
#proyecto = "com.unida"
#print(f"Se hara en {app} y el proyecti se llama {proyecto}")

'''
Crear un programa que pida dos numeros
y obtenga como resultado cual de ellos es par o si 
ambos los son
'''
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

while numero1 != 0 or numero2 % 2 == 0:
    if ((numero1 % 2 == 0) and (numero2 % 2 == 0)):
        print("Ambos numeros son par!")
    elif ((numero1 % 2 == 0) and (numero2 % 2 != 0)):
        print("El numero {numero1} es par")
        print("El numero {numero2} es impar")
    elif ((numero1 % 2 != 0) and (numero2 % 2 == 0)):
            print("El numero {numero1} es impar")
            print("El numero {numero2} es par")
    else:
        print("Ninguno es par")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))