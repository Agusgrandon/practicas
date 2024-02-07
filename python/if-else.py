a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))

if b != 0:
    division = a / b
    print("El resultado es: ", division)
else:
    print("No se puede dividir por 0")
print("chau")

#if else
x = int(input("Ingresa un numero: "))

if x != 0:
    if x > 0:
        resultado = "positivo"
    else:
        resultado = "negativo"
else: 
    resultado = "neutro"
print(x,"es",resultado)