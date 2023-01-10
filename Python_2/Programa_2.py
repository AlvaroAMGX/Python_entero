#22
#Crea una aplicación que permita adivinar un número. La aplicación genera un
#número aleatorio del 1 al 100. A continuación, va pidiendo números y va
#respondiendo si el número a adivinar es mayor o menor que el introducido, a
#demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
#programa termina cuando se acierta el número (además te dice en cuantos
#intentos lo has acertado), si se llega al limite de intentos te muestra el número
#que había generado.
#Alvaro Medel García
#Aqui hay tres variables para el número aleatorio,el contador para que solo sean 10 veces y otro para que introduzcas el numero y se vaya comparando.

import random
numaleatorio=int(random.uniform(0,100))
contador=0
num=int(input("Dime un número:"))
while num!=numaleatorio and contador<=9:
    contador=contador+1
    if num==numaleatorio:
        print("Has acertado")    
        break
    elif num>numaleatorio:
        print("El número es menor")
        print("Vas por el intento ",contador)
    elif num<numaleatorio:
            print("El número es mayor")
            print("Vas por el intento ",contador)
    num=int(input("Dime otro número número:"))
    if contador==10:
        print("No has acertado mas suerte la proxima vez")
