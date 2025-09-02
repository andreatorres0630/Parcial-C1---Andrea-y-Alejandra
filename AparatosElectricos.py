# En El Salvador, muchas familias desean controlar su gasto eléctrico mensual. Cada hogar utiliza distintos aparatos eléctricos, como refrigeradores, televisores, 
# aire acondicionado o iluminación, durante diferentes cantidades de horas. Sin un registro, es difícil saber qué aparato genera mayor consumo y cómo optimizar 
# el gasto mensual de electricidad. 
# Se busca un sistema que permita registrar los aparatos utilizados, calcular automáticamente el consumo y el costo de cada uno, y generar una salida en pantalla 
# al final que muestre los datos ordenados de cada aparato. Además, el sistema debe mostrar un resumen con el consumo total y el gasto mensual.

# Crear primero la clase Aparatos Electricos que serviran para almacenar cada aparato 
class AparatosElectricos:
    # Lista estática para almacenar todos los aparatos registrados
    listado = []

    def __init__(self, nombre, potenciaWatts, horas_diarias, preciokWh):
        # Explicación de cada uno 
        # nombre: Es el nombre del aparato
        # potenciaWatt: Es la potencia del aparato en Watts
        # horas_diarias: Son las horas que el aparato se utiliza al día
        # preciokWh: Es el precio del kWh en dólares
       
        self.nombre = nombre
        self.potenciaWatts = potenciaWatts
        self.horas_diarias = horas_diarias
        self.preciokWh = preciokWh

        # Se calcula automáticamente el consumo y el costo mensual
        self.consumo_mensual = self.calcular_consumo()
        self.costo_mensual = self.calcular_costo()

        # Agregamos el aparato al listado general
        AparatosElectricos.listado.append(self)

    def calcular_consumo(self):
        # Calcula el consumo mensual en kWh.
        return round((self.potenciaWatts * self.horas_diarias * 30) / 1000, 2)

    def calcular_costo(self):
        # Calcula el costo mensual del aparato.
        return round(self.consumo_mensual * self.preciokWh, 2)


    def info(self):
        # Este devuelve una cadena con la información del aparato que se ingresa
        return (f"Aparato eléctrico: {self.nombre} | Potencia: {self.potenciaWatts} W | "
                f"Horas diarias: {self.horas_diarias} | Consumo: {self.consumo_mensual} kWh | "
                f"Costo mensual: ${self.costo_mensual}")
