#17
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El
#tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un
#algoritmo que determine la hora de llegada a la ciudad B.
#Alvaro Medel García
#Hay varias variables son para guardar el tiempo,la duración del viaje y despues donde hago los calculos para decirle cuando llega.
horas=int(input("Dime la hora: "))
minutos=int(input("Dime los minutos: "))
segundos=int(input("Dime los segundos: "))
duracion=int(input("Dime la duración del viaje en segundos: "))
Total=horas*3600+minutos*60+segundos+duracion
horas=Total//3600
segundosrestantes=Total%3600
minutos=segundosrestantes//60
segundos=segundosrestantes%60
print("La hora de llegada es",horas,":",minutos,":",segundos)

