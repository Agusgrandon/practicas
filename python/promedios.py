numeros = 5
sumatoria = 0

for cont in range(1,numeros+1):
    print("ingrese un numero ", cont)
    num = int(input())
    sumatoria += num

print("la suma es ", sumatoria)
print("el promedio es ", sumatoria/numeros)

########
#ej acumulador 

n = 100
sumatoria_dos = 0

for cont_dos in range(1,n +1):
    sumatoria_dos = sumatoria_dos + cont_dos

print(sumatoria_dos)
