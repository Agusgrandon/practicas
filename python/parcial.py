contador_inicial = 0
#Informe A- Cuál fue el sexo menos ingresado (F o M)
contador_femenino = 0
contador_masculino = 0
#Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
contador_tipo_gato = 0
contador_tipo_perro = 0
contador_tipo_exotico = 0
#Informe E- El promedio de peso de todas las mascotas
acumululador_de_peso = 0


while contador_inicial < 3 :

    nombre = input("ingresa el nombre de la mascota: ")

    tipo = input("ingresa el tipo de la mascota: ")
    while tipo != "gato" and tipo != "perro" and tipo != "exotico":
        tipo = input("error, ingresa el tipo de la mascota: ")

    peso = input("ingresa el peso de la mascota: ")
    peso = int(peso)
    while peso < 10 or peso > 80 :
        peso = input("error, ingresa el peso de la mascota: ")
        peso = int(peso)

    sexo = input("ingresa el sexo de la mascota: ")
    while sexo != "femenino" and sexo != "masculino" :
        sexo = input("ingresa el sexo de la mascota: ")

    edad= input("ingresa el edad de la mascota: ")
    edad = int(edad)
    while edad < 1 :
       edad= input("error, ingresa la edad de la mascota: ")
       edad = int(edad)
    
    match sexo :
        case "femenino":
            contador_femenino += 1
        case "masculino":
            contador_masculino += 1

    match tipo :
        case "gato":
            contador_tipo_gato += 1
        case "perro": 
            contador_tipo_perro += 1
                #Informe D- El nombre del perro más joven
            if contador_inicial == 0 or edad < mascota_joven:
                mascota_joven = edad
                mascotas_mas_joven = nombre
        case "exotico":
            contador_tipo_exotico += 1

    #Informe C- El nombre y tipo de la mascota menos pesada
    if contador_inicial == 0 or peso < mascota_menos_pesada:
        mascota_menos_pesada = peso
        nombre_mascota_menos_peso = nombre
        tipo_mascota_menos_peso = tipo

            
    acumululador_de_peso  += peso
    contador_inicial += 1



porcentaje_gatos = (contador_tipo_gato * 100) / contador_inicial
porcentaje_perro = (contador_tipo_perro * 100 ) / contador_inicial
porcentaje_exotico = (contador_tipo_exotico * 100) / contador_inicial

##Informe E- El promedio de peso de todas las mascotas
promedio_peso_de_los_animales = acumululador_de_peso / contador_inicial


if contador_femenino < contador_masculino:
    sexo_menos_ingresado = "femenino"
else:
    sexo_menos_ingresado = "masculino"


mensaje = (f"el sexo menos ingresado fue {sexo_menos_ingresado}.\n"
           f"el porcentaje ingresado de gatos es {porcentaje_gatos}%, el porcentaje ingresado de perros es {porcentaje_perro}%, el porcentaje ingersado de exoticos es {porcentaje_exotico}%.\n"
           f"la mascota que menos peso fue {nombre_mascota_menos_peso}, del tipo {tipo_mascota_menos_peso}.\n"
           f"el perro mas joven es {mascotas_mas_joven}.\n"
           f"el promedio de peso de los animales es de: {promedio_peso_de_los_animales}")
print(mensaje)
