#20
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
#después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20
#céntimos o 10 céntimos).
#Alvaro Medel García.
#En este ejercicio las variables son para guardar las monedas y hacer el calculo.
dos=int(input("cuantas monedas de dos euros tienes:"))
uno=int(input("cuantas monedas de un euro tienes:"))
cincuenta=int(input("cuantas monedas de cincuenta céntimos tienes:"))
veinte=int(input("Dime el numero de dos cifras "))
diez=float(input("Dime el numero de dos cifras "))
euros='%.2f'%((dos*2)+(uno)+(cincuenta*0.50)+(veinte*0.20)+(diez*0.10))
print("Tienes ",euros," euros")
