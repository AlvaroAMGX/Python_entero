#17
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al
#lanzar un dado de seis caras y muestre por pantalla el número en letras (dato
#cadena) de la cara opuesta al resultado obtenido. Nota 1: En las caras opuestas
#de un dado de seis caras están los números: 1-6, 2-5 y 3-4. Nota 2: Si el número
#del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje:
#"ERROR: número incorrecto.".
#Alvaro Medel García
#Tenemos una sola variable que segun sea un número o otro nos devolvera el otro lado del dado
num=int(input("Dime el número del dado:"))
if num==6:
    print("El lado contrario es 1.")
if num==5:
    print("El lado contrario es 2.")
if num==4:
    print("El lado contrario es 3.")
if num==3:
    print("El lado contrario es 4.")
if num==2:
    print("El lado contrario es 5.")
if num==1:
    print("El lado contrario es 6.")
if num>6 or num<1:
    print("ERROR: número incorrecto.")
