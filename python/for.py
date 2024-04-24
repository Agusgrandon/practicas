'''
for <variable que oficia de contadora> in range (el valor de fin  sin incluir):
    instrucciones
'''
for variable in range (1, 11): #va a tomar del 1 al 10
    print(variable, "hola")

numero = int(input("ingrese un numero "))

for c in range(1, 11):
    print(numero, "x", c, "=", (numero * c))