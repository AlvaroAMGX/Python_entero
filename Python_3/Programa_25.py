#25
#Alvaro Medel García
#Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es el siguiente:
#Se divide el número mayor entre el menor.
#Si la división es exacta, el divisor es el MCD.
#Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
#Crea un programa principal que lea dos números enteros y muestre el MCD.
def Intercambiar(mayor,menor):
	if mayor<menor:
		return menor,mayor
	else:
		return mayor,menor
def CalcularMCD(num1,num2):
	num1, num2 = Intercambiar(num1,num2)
	resto = num1 % num2
	if resto == 0: 
		return num2
	else:
		return CalcularMCD(num2,resto)
numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
print("MCD: ", CalcularMCD(numero1,numero2))
