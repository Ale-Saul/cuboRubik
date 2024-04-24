1. Nombre: Alejandro Saul Montaño Cespedes
2. Breve descripcion del proyecto:
El solucionador del Cubo Rubik 3x3 es una aplicación desarrollada en Python que permite resolver automáticamente el famoso rompecabezas
tridimensional. El algoritmo utilizado para encontrar la solución es el A*, que es un algoritmo de búsqueda heurística ampliamente utilizado
en inteligencia artificial y resolución de problemas. Este solucionador utiliza una representación del cubo en forma de objeto y emplea técnicas
de búsqueda y optimización para encontrar la secuencia de movimientos necesarios para resolver el cubo desde cualquier configuración inicial
hasta el estado resuelto. Con una interfaz simple y eficiente, este solucionador proporciona una herramienta útil para aficionados y entusiastas
del Cubo Rubik que buscan mejorar sus habilidades de resolución y comprender mejor los principios detrás de este desafiante rompecabezas.
3. Requerimientos del entorno de programacion:
El proyecto del Solucionador del Cubo Rubik 3x3 está desarrollado en Python y requiere un entorno de programación compatible con este lenguaje de programación. A continuación se detallan los requerimientos del entorno de programación necesarios para ejecutar y desarrollar el proyecto:
Python: Se requiere Python 3.12.2 para ejecutar el solucionador del Cubo Rubik 3x3. Se recomienda utilizar la última versión estable de Python disponible.
Bibliotecas de Python: El proyecto hace uso de ciertas bibliotecas de Python para el manejo de datos y la implementación del algoritmo A*. Asegúrese de tener instaladas las siguientes bibliotecas:
heapq: Utilizada para implementar la cola de prioridad requerida por el algoritmo A*.
Otras bibliotecas estándar de Python, como copy y sys, pueden ser utilizadas en el proyecto.
Ambiente virtual (opcional): Se recomienda utilizar un ambiente virtual para aislar las dependencias del proyecto y evitar conflictos con otros proyectos. Puede utilizar herramientas como virtualenv o conda para crear y gestionar ambientes virtuales.
Editor de texto o entorno de desarrollo integrado (IDE): Se puede utilizar cualquier editor de texto o IDE compatible con Python para desarrollar el proyecto. Algunas opciones populares incluyen Visual Studio Code, PyCharm y Sublime Text.
Control de versiones: Se recomienda utilizar un sistema de control de versiones como Git para gestionar el código fuente del proyecto y colaborar con otros desarrolladores. Asegúrese de tener Git instalado en su sistema y configurado correctamente.

5. Manual de uso
   4.1.Formato de codificación para cargar el estado de un cubo desde el archivo de texto
   El tipo de archivo que soporta el programa es el siguiente:
   
    WYR
    YWB
    WBW
    BRY
    YYW
    BRR
    BRG
    BRO
    YWO
    YRO
    GOY
    YGW
    GOR
    GGO
    OBO
    RWG
    WBO
    GGB
  Tener en cuenta que primero debe ir la cara W, seguida de la Y, R, O, G y B. Igual el programa no aceptara que el cubo no tenga las piezas completas o que los centros esten cambiados
  igual que debe tener el archivo 18 lineas.
   4.2.Instrucciones para ejecutar el programa
     Al iniciar el programa con el comando py main.py se mostrara un menu con las opciones que se tienen el menu e el siguiente:
         1. Mostrar cubo
         2. Desarmar cubo predeterminado
         3. Mover cubo
         4. Resolver cubo
         5. Reiniciar cubo
         6. Obtener soluciones suboptimas
         7. Cargar cubo desde archivo
         8. Resolver cubo de archivo
         9. Mostrar Cubo de archivo
         10. Obtener soluciones suboptimas del cubo del archivo
         0. Salir
7. Diseño e implementación
  5.1.Breve descripción de modelo del problema
   El modelo del Cubo Rubik está representado como un diccionario en Python, donde cada cara del cubo se representa como una matriz tridimensional. Por ejemplo:
   cube_model = {
    'U': [['W']*3 for _ in range(3)],
    'D': [['Y']*3 for _ in range(3)],
    'F': [['R']*3 for _ in range(3)],
    'B': [['O']*3 for _ in range(3)],
    'L': [['G']*3 for _ in range(3)],
    'R': [['B']*3 for _ in range(3)]
     }
  5.2.Explicación y justificación de algoritmo(s), técnicas, heurísticas seleccionadas.
   El algoritmo utilizado para resolver el Cubo Rubik es A*, una técnica de búsqueda heurística ampliamente utilizada en inteligencia artificial y resolución de problemas. La heurística empleada se      basa en el conteo de las aristas y esquinas mal orientadas del cubo, lo que proporciona una estimación del grado de desorden del cubo y guía la búsqueda hacia una solución óptima.
  5.3.En caso de usar modelos lingüísticos, incluir los prompts clave
   "¿Cómo puedo resolver el Cubo Rubik?"
   "¿Cuál es el siguiente movimiento para completar la primera capa?"
   "Indica el algoritmo utilizado para resolver el Cubo Rubik."
   "¿Qué estrategias heurísticas se emplean en el algoritmo A*?"
   "Describe el modelo del problema utilizado para representar el Cubo Rubik."
8. Trabajo Futuro
    6.1.Lista de tareas inconclusas y/o ideas para continuar con el proyecto
      Optimización del Algoritmo A*
      Interfaz Gráfica de Usuario (GUI)
      Extensión a Otros Tamaños de Cubo
      Refinamiento de la Heurística















   
