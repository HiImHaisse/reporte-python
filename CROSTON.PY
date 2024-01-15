def pronostico_croston(demandas):
    # Código para el pronóstico Croston
    demandas = list(map(float, demandas))  # Convertir las demandas a números flotantes
    
    if len(demandas) != 5:
        print("Se requieren 5 datos de demanda para el pronóstico Croston.")
        return
    
    # Realizar cálculos de pronóstico Croston para la semana 6
    # Aquí puedes implementar tu lógica específica de pronóstico Croston
    
    pronostico = sum(demandas) / len(demandas)  # Ejemplo de pronóstico simple, promedio de las demandas
    
    print("El pronóstico Croston para la semana 6 es:", pronostico)

def pronostico_stb():
    # Código para el pronóstico STB
    print("Has seleccionado Pronóstico STB")

while True:
    print("Menú:")
    print("1. Pronóstico Croston")
    print("2. Pronóstico STB")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        demandas = []
        for i in range(5):
            demanda = input(f"Ingrese la demanda para la semana {i+1}: ")
            demandas.append(demanda)
        pronostico_croston(demandas)
    elif opcion == "2":
        pronostico_stb()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")