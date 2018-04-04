#Creo e inicializo las variables
x = 0
y = 0
z = 0

#Pregunto tres números
x = int(input("Dime un número mayor que 0:\n"))
if x > 0:
	y = int(input ("Dime ahora un número mayor que el anterior:\n"))
	if y > x:
		z = int(input ("Dime ahora otro número pero que sea menor que 0:\n"))
		if z < 0:
			print(x, " + ", y, " + ", z, "=",x + y + z)
		else:
			print ("Error")
	else:	
		print ("Error")
else:
	print ("Error")
