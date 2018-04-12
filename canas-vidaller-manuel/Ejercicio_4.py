#Creo e inicializo las variables
import time
num = 0

#Pregunto un número para la cuenta atrás
num = int(input("Dime un número para la cuenta atrás:\n"))

#Se inicia la cuenta atrás
for i in range(1,num):
	print (num-i)
	#Paramos el tiempo 0.5s
	time.sleep(0.5)

#Indicar que el cohete a despegado
print ("¡¡El cohete a despegado!!")