#nombre_de_usuario = input("Ingresa tu nombre: ")
#print("Hola",nombre_de_usuario,"!",sep="$")

#concatenar valores fuera de la funcion print es posible solo con el +
nombre_de_usuario = input("Ingresa tu nombre: ")
saludo = "Hola " + nombre_de_usuario + "!"
print(saludo)

#coloco el str para convertirlo en cadena
edad = int(input("Ingresa tu edad: "))
saludo2 = "Tenes "+ str(edad) + " años"
print(saludo2)

#tambien se puede asi
edad_de_usuario = int(input("Ingresa tu edad: "))
print("Tenes ",edad_de_usuario," años")

#mostrar por consola la frase 
descartes = input("descartes dijo: ")
conclusion = "Descartes dijo: " + descartes
print(conclusion)
#tambien se puede asi
print("Descartes dijo: \"Pienso luego existo\"")
#salto de linea
print("uno\ndos\ntres")
#salto de tabulacion
print("uno\tDos\tTres")