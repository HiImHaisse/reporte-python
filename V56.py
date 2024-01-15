import pandas as pd

def pronostico_croston(demandas):
    # Código para el pronóstico Croston
    demandas = list(map(float, demandas))  # Convertir las demandas a números flotantes
    
    if len(demandas) != 5:
        print("Se requieren 5 datos de demanda para el pronóstico Croston.")
        return
    
    # Realizar cálculos de pronóstico Croston para las primeras 5 semanas
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
        archivo = input("Ingrese la ruta del archivo Excel: ")
        
        try:
            df = pd.read_excel(archivo)
            demandas = df.iloc[:5, 0].tolist()  # Obtener las primeras 5 filas de la primera columna como demandas
            pronostico_croston(demandas)
        except FileNotFoundError:
            print("Archivo no encontrado.")
        except Exception as e:
            print("Ocurrió un error al leer el archivo:", str(e))
            
    elif opcion == "2":
        pronostico_stb()
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")