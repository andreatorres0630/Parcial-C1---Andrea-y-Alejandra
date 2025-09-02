# En El Salvador, muchas familias desean controlar su gasto eléctrico mensual. Cada hogar utiliza distintos aparatos eléctricos, como refrigeradores, televisores, 
# aire acondicionado o iluminación, durante diferentes cantidades de horas. Sin un registro, es difícil saber qué aparato genera mayor consumo y cómo optimizar 
# el gasto mensual de electricidad. 
# Se busca un sistema que permita registrar los aparatos utilizados, calcular automáticamente el consumo y el costo de cada uno, y generar una salida en pantalla 
# al final que muestre los datos ordenados de cada aparato. Además, el sistema debe mostrar un resumen con el consumo total y el gasto mensual.


from AparatosElectricos import AparatosElectricos  #Importamos la clase AparatosElectricos

class GestionConsumo:

    def mostrar_registros():
        # Muestra todos los aparatos registrados, ordenados por consumo mensual.
        # Si no hay aparatos registrados, se muestra un aviso aqui
        if not AparatosElectricos.listado:
            print("No hay aparatos registrados")
            return
        print("LISTADO DE APARATOS ELÉCTRICOS ORDENADOS POR CONSUMO")
        print("-" * 70)
        # Ordenamos los aparatos de mayor a menor consumo
        aparatos_ordenados = sorted(AparatosElectricos.listado, key=lambda x: x.consumo_mensual, reverse=True)

        # y Mostramos cada aparato con toda su información
        for i, aparato in enumerate(aparatos_ordenados, 1):
            print(f"{i}. {aparato.info()}")


    def mostrar_resumen():
        # Muestra un resumen ya incluyendo lo que es el consumo y el gasto total.
        # Si no hay datos, se muestra un aviso
        if not AparatosElectricos.listado:
            print("No hay datos para mostrar")
            return

        # Sumamos todos los consumos y costos
        consumo_total = sum(a.consumo_mensual for a in AparatosElectricos.listado)
        gasto_total = sum(a.costo_mensual for a in AparatosElectricos.listado)

        # Mostramos el resumen general
        print("-----------RESUMEN GENERAL----------")
        print("-" * 40)
        print(f"El consumo total mensual es de: {consumo_total:.2f} kWh")
        print(f"El gasto total mensual es de: ${gasto_total:.2f}")
        print("-" * 40)
