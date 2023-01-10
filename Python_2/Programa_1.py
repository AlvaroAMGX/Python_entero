#4
#Crea un programa que pida al usuario dos números y muestre su división si el
#segundo no es cero, o un mensaje de aviso en caso contrario.
#Alvaro Medel García
#Tenemos dos variables para los números dependiendo de si el segundo es cero hace una cosa o otra.
uno=int(input("Dime el primer número:"))
dos=int(input("Dime el segundo número:"))
if dos!=0:
    print("La división es",uno/dos)
else:
    print("El segundo número es cero")


