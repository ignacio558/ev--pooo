#mostrar todos los valores del vehiculo
#Calcula la distancia recorrida, con los datos obtenidos anteriormente. Debes mostrar cuál es el total a pagar por dicha carrera.
#Al finalizar la carrera, entonces se deberá ingresar la ubicación GPS, del destino.
from datetime import datetime
import math
velo = 0 # Definimos la velo inicial
pi = math.pi 
lati1 = 0
log1 = 0

def Distancia(lat1, log1, lat2, log2):
    #busque el radio de la para asi calcular la distancia
    radio = 6371 #km
    # convertir las cordenadas a radiantes
    lat = (lat2 - lat1) * (math.pi / 180)
    log= (log2 - log1) * (math.pi / 180)

    a = (math.sin(lat / 2) * math.sin(lat / 2)) + (math.cos(lat1 * (math.pi / 180)) * (math.cos(lat2 * (math.pi / 180)))) * (math.sin(log / 2) * math.sin(log / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    dis = radio*c
    return dis
print
print("*************************************************")
print("*                                               *")
print("*    agregue los datos para registrarse.        *")
print("*                                               *")  
print("*************************************************")
usuario = input("ingrese su nombre de usuario:  ")
correo = input("Ingrese su correo:  ")
clave = input("Ingrese una clave: ")
edad = int(input("Ingrese su edad:  "))
patente = input("Ingrese su patente del vehiculo:   ")
if edad < 18:
    print("No puede ingresar porque es menor de edad\n")
elif edad >= 18:
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("su nombre de usuario es:", usuario,", su correo es:", correo,", su edad es:", edad,", su patente es:", patente, ", usted se registro el :", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("1.- para iniciar sesion. ")
    print("2.- para comenzar una carrera ")
    opc = input()
    if opc == "1":
        verficacionCorreo = input("Ingrese su correo electronico:\n")
        verficacionclave = input("Ingrese su clave:\n")
        if verficacionCorreo == correo and verficacionclave == clave:
            print(" Bienvenido", usuario, ", patente numero", patente, datetime.now().strftime("Dia %d del %m del %Y %H:%M:%S"))
            opcion = ""
            encendido = False
            carrera = input("Presione 1 para comenzar una carrera\nPresione 2 para salir\n")
            if carrera == "1":
                while opcion != "8":
                    print("1. - Ingresar ubicación GPS , LATITUD")
                    print("2. - Ingresar ubicación GPS , LONGITUD")
                    print("3. - Encender el vehículo.")
                    print("4. - Acelerar vehículo")
                    print("5. - Bajar velocidad del vehículo")
                    print("6. - Apagar Vehículo")
                    print("7. - Girar Vehículo.")
                    print("8. - Terminar la carrera.")
                    opcion = input()
                    if opcion == "1":
                        lati1 = float(input("Ingrese la latitud:\n"))
                        print("*************************************************")
                        print("    Latitud ingresada correctamente\n          ")
                        print("*************************************************")
                    elif opcion == "2":
                        log1 = float(input("Ingrese la longitud:\n"))
                        print("*************************************************")
                        print("   Longitud ingresada correctamente\n         ")
                        print("*************************************************")
                    elif opcion == "3":
                        print("vehiculo encendido \n")
                        encendido = True
                    elif opcion == "4" and encendido:
                        velo += 10
                        print("*************************************************")
                        print("el vehiculo esta viajando a", velo, "Km/h\n")
                        print("*************************************************")
                    elif opcion == "5" and encendido:
                        if velo < 10:
                            print("*************************************************")
                            print("el vehiculo esta detenido\n")
                            print("*************************************************")
                        elif velo >= 10:
                            if velo == 10:
                                velo = 0
                                print("*************************************************")
                                print("el vehiculo esta detenido\n")
                                print("*************************************************")
                            elif velo > 10:
                                velo -= 10
                                print("*************************************************")
                                print("el vehiculo esta viajando a: ", velo, "Km/h\n")
                                print("*************************************************")
                    elif opcion == "6" and encendido:
                        print("*************************************************")
                        print("el vehiculo esta apagado \n")
                        print("*************************************************")
                        encendido = False
                    elif opcion == "7" and encendido:
                        print("*************************************************")
                        print("Girando vehículo...\n")
                        print("*************************************************")
                    elif opcion == "8":
                        print("*************************************************")
                        print("Terminando carrera...\n")
                        print("*************************************************")
                        lati2 = float(input("Ingrese la latitud de su  destino:\n"))
                        log2 = float(input("Ingrese la longitud de su destino:\n"))
                        distancia = Distancia(lati1, log1, lati2, log2)
                        print("Distancia recorrida:", round(distancia, 2), "Km")
                        print("El Total a pagar por la carrera es de : $", round(distancia*(550*1.8))) 
                    else:
                        print("opción no válida\n")
            elif carrera == "2":
                print("Gracias por usar el sistema")
            else:
                print("La no es opción es válida\n")
        else:
            print("Correo o clave incorrectas :( \n")
    elif opc == "2":
        print("debe registrarse antes de inciar la carrera\n")
    else:
        print(" La opción no es válida\n")