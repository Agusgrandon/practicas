print("Menu de opciones")
print("[1] ventas")
print("[2] soporte")
print("[3] administracion")

opcion = int(input("Elegir opcion: "))

match opcion: 
    case 1:
        print("Ventas")
    case 2:
        print("soporte")
    case 3:
        print("administracio")
    case _:
        print("opcion inexistente")
##############################################################################
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

print("[+]")
print("[-]")
print("[x]")
print("[/]")

simbolo = input("Ingrese la operacion: ")

match simbolo:
    case "+":
        print("Reusltado: ", (a + b))
    case "-":
        print("Reusltado: ", (a - b))
    case "x":
        print("Reusltado: ", (a * b))
    case "/":
        #no se puede dividir por 0
        if b != 0:
            print("Reusltado: ", (a / b))
        else:
            print("No se puede dividir por 0") 
    case _:
        print("opcion inexistente")