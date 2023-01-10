#24
#Alvaro Medel García
#Crear una función recursiva que permita calcular el factorial de un número. 
#Realiza un programa principal donde se lea un entero 
#y se muestre el resultado del factorial.
def CalcularFactorial(num):
	if num == 1:
		return 1
	else:
		return num*CalcularFactorial(num-1)
numero1 = int(input("Número:"))
print("El factorial es:",CalcularFactorial(numero1))
