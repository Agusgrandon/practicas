print(5+2)
print(9-5)
print(9*5)
print(9/5)
#division entera
print(9//5)
#potencia
print(9**5)
#modulo o residuo
print(9%5)

numeroUno = int(input("Ingresa un numero: "))
numeroDos = int(input("Ingresa otro numero: "))
print("El resultado es: ", numeroUno + numeroDos)

#calcular la edad
anioActual = 2024
fechaDeNacimiento = int(input("Ingresa tu año de nacimiento: "))
edad = anioActual - fechaDeNacimiento
print("Tu edad es: ", edad)

#entrada
ancho = int(input("Ingresa ancho del terreno: "))
alto = int(input("Ingresa alto del terreno: "))
precio_m2 = int(input("Ingresa precio del terreno: "))
#proceso
superficie = ancho * alto
precioTerreno = superficie * precio_m2
#salida
print("El precio del terreno es: ", precioTerreno)

# < menor que 
# <= menor o igual que
# > mayor que 
# >= mayor o igual que 
# == igual que 
# != distinto que 

# Y / AND : conjuncion
# 0 / OR : disyuncion simple 
# NO : negacion

#porcentaje
precio = 500

# 500_ 100%
#  x_ 21 % = 500 * 21 / 100
aumentoIva = precio * 21 / 100

precio_final = precio + aumentoIva #o precio + (precio * 0.21) ó precio * 1.21

mensaje = f"el precio es de {precio} se aplico iva {aumentoIva} quedo un total de {precio_final}"

print("factura", mensaje)

# Jerarquia de operadores:
# ()
# *
# * // / %
# +-
# < > etc
# not
# and 
# or 