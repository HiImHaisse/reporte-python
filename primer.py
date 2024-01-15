#Primer ejercicio de python 
def pronosticos_croston():
    print("Has seleccionado pronóstico Croston")

def pronosticos_stb():
    print("Has seleccionado pronostico STB")

while True:
    print("Menu")
    print("1. Pronostico croston")
    print("2. Pronostico STB")
    print("3. Salir")
    opcion= input ("Elegir una opción")
    if opcion =="1":
        pronosticos_croston()
    elif opcion =="2":
        pronosticos_stb()
    elif opcion =="3":
        break
    else:
        print("Opción invalidad . Por favor, elive una opción valida.")