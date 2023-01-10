#18
#Alvaro Medel García
#Crea un programa que pida dos número enteros al usuario 
# y diga si alguno de ellos es múltiplo del otro. 
# Crea una función EsMultiplo que reciba los dos números, 
# y devuelve si el primero es múltiplo del segundo.
def Esmultiplo(num1,num2):
    if num1%num2==0:
        return True
    else:
        return False 
numero1=int(input("Dime un número: "))
numero2=int(input("Dime otro número: "))
if Esmultiplo(numero1,numero2)==True:
    print("El primer número es multiplo del segundo")
else:
    print("Ninguno de los números es multiplo")