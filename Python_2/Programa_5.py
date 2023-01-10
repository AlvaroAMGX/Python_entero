#7
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y
#el exponente. Pueden ocurrir tres cosas:
#   1. El exponente sea positivo, sólo tienes que imprimir la potencia.
#   2. El exponente sea 0, el resultado es 1.
#   3. El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
#Alvaro Medel García
#Aqui tendremos dos variables una para el exponente y otra base y segun como se se hara una cosa o otra.
exponente=int(input("Dime el exponente: "))
base=int(input("Dime la base: "))
if exponente>0:
    print("La potencia es ",base**exponente)
else:
    if exponente==0:
        print("La pontencia es 1")
    else:
        print("La potencia es" ,1/(base**abs(exponente)))