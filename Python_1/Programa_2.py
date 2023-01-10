#7
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla
#a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16
#horas y 40 minutos.
#Alvaro Medel García
#Se usan tres variables para los minutos que se introducen y las horas y minutos que son esos minutos 
min=int(input("Introduce los minutos:"))
horas=(min//60)
minutos=min%60
print("Son ",horas ,"horas y ",minutos," minutos")