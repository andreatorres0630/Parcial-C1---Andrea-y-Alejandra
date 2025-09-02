Integrantes:
  - Andrea Melissa Torres Batres
  - Alejandra María Baires Campos

Preguntas:

1. ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?
La solución presentada está dividida en módulos (archivos separados):

AparatosElectricos.py → define la clase y la lógica de cálculo.
Gestion.py → maneja la gestión de los registros y el resumen.
Main.py → contiene la interfaz con el usuario (menú).

Ventajas:
Organización: el código queda más estructurado y fácil de leer.
Reutilización: la clase AparatosElectricos se puede usar en otros proyectos sin modificar el resto.
Mantenimiento: si se necesita corregir un error o agregar funciones, basta con modificar un módulo sin afectar todo el sistema.
Escalabilidad: facilita agregar nuevas funcionalidades (por ejemplo, reportes en PDF) sin necesidad de alterar el archivo principal.


2. ¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describan el papel de las clases creadas.

Se aplicó POO mediante la creación de la clase AparatosElectricos, la cual cumple con los principios de encapsulación y abstracción.
Clase AparatosElectricos:
Representa a cada aparato eléctrico como un objeto con atributos (nombre, potenciaWatts, horas_diarias, preciokWh).
Contiene métodos que realizan operaciones específicas (calcular_consumo, calcular_costo, info).
Mantiene un listado estático donde se registran todos los aparatos creados, lo que permite gestionarlos fácilmente.

Clase GestionConsumo:
Se encarga de procesar la información de los objetos de tipo AparatosElectricos.
Ordena y muestra el listado de aparatos según el consumo.
Calcula los totales de consumo y gasto mensual.

Clase Main:
Sirve como la interfaz con el usuario.
Contiene el menú principal y recibe las entradas (nombre, potencia, horas de uso, etc.).
A través de este archivo se crean los objetos AparatosElectricos y se llaman los métodos de GestionConsumo.
De esta forma, separamos la lógica del sistema de la interacción con el usuario.


3. ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto.

El uso de GitHub nos facilitó el trabajo colaborativo porque nos permitió organizarnos mejor y trabajar al mismo tiempo sin afectar el código de la otra.
Ejemplo concreto:
Mientras yo trabajaba en la clase AparatosElectricos.py definiendo los atributos y métodos, mi compañera Andrea desarrollaba las funciones de gestión en Gestion.py. Después, subimos nuestros cambios a GitHub y el sistema integró todo en un solo proyecto sin necesidad de copiar y pegar archivos. 
Además, si cometíamos un error, podíamos regresar a una versión anterior fácilmente.
