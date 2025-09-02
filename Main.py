# En El Salvador, muchas familias desean controlar su gasto eléctrico mensual. Cada hogar utiliza distintos aparatos eléctricos, como refrigeradores, televisores, 
# aire acondicionado o iluminación, durante diferentes cantidades de horas. Sin un registro, es difícil saber qué aparato genera mayor consumo y cómo optimizar 
# el gasto mensual de electricidad. 
# Se busca un sistema que permita registrar los aparatos utilizados, calcular automáticamente el consumo y el costo de cada uno, y generar una salida en pantalla 
# al final que muestre los datos ordenados de cada aparato. Además, el sistema debe mostrar un resumen con el consumo total y el gasto mensual.

from AparatosElectricos import AparatosElectricos
from Gestion import GestionConsumo

def menu():
    print("---------------SISTEMA DE CONTROL DE GASTO ELÉCTRICO---------------")
    print("1. Registrar un nuevo aparato eléctrico")
    print("2. Mostrar el listado de aparatos eléctricos")
    print("3. Mostrar resumen general")
    print("4. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del aparato: ")
            potencia = float(input("Ingrese la potencia en Watts: "))
            horas = float(input("Ingrese horas de uso diario: "))
            precio_kwh = float(input("Ingrese el precio por kWh ($): "))

            AparatosElectricos(nombre, potencia, horas, precio_kwh)
            print("Aparato registrado.")

        elif opcion == "2":
            GestionConsumo.mostrar_registros()
        elif opcion == "3":
            GestionConsumo.mostrar_resumen()
        elif opcion == "4":
            print("¡Gracias por utilizar el sistema!")
            break
        else:
            print("Opción inválida, intente de nuevo.")
