# Informe-de-venta 📈
### Descripción:
- Proyecto integrador en Python inicial que consiste mediante entrada de datos de cliente, producto y ventas poder generar reportes de ventas, tendencia de consumo y gastos historico de cada cliente.
- El Programa contiene 8 funciones, la primera ingresa clientes al sistema, es decir, crea un nuevo cliente, con su propio identificació(ID) unica e irrepetible, siempre y cuando no se elimine el archivo creado con anterioridad. La cuarta opcion ingresa productos, cada producto tiene su propio codigo que lo identifica.
- La sexta opcion es para ingresar las ventas. Dicha opcion no podra ser ejecutada si no se crean con anterioridad las opcion 1 y 4. En caso contrario automaticamente se solicitara la creación de ambos archivos puesto que es indispensable para la venta, sin cliente o producto no hay venta.
- La septima y octava opcion es para mostrar los reporte, una para reporte de cada cliente de caso particular y otra con ventas general del negocio respectivamente
### Pre-requisitos: 
- El lenguaje del programa esta escrito en Python por lo que es necesario instalar el lenguaje previamente para poder utilizarlo
- (Opcional) Descargar e instalar un editor de código como Visual Estudio Code 
### Ejecución:
- Se requiere clonar el repositorio para poder utilizar el programa: 
    * Para clonarlo desde consola primero se debe ubicar en la carpeta donde desee guardar el programa. Luego debe ingresar la linea git clone junto la URL que desee clonar, en    este caso:
    ```
    git clone https://github.com/alejandrorodriguezsalas/Informe-de-venta
    ```  
    ![Clonación](/Imagenes/Git%20clone%20Informe-de-venta.png)

   * Otra forma es simplemente puede descargar el archivo zip desde el boton verde de arriba
    1. Paso1: 
       ![Descarga1](/Imagenes/Descargar%20paso%201.png)
    2. Paso2: 
       ![Descarga1](/Imagenes/Descargar%20paso%202.png)
    

- Se agrega al repositorio 3 archivos, Cliente.csv, Producto.csv y Ventas.csv como ejemplo. Para ingresar datos desde cero solo hace falta eliminar esos 3 archivos y ejecutar el programa. Los programas más importante son proyecto.py y funciones_alejandro.py

- Se puede ejecutar de dos formas:
    1. (RECOMENDADA) Desde windows entrando a simbolo de sistema (cmd): Ubicado dentro de la carpeta Informe-de-venta se debe agregar la linea
    ```
    python proyecto.py
    ```
    
    ![Ejecución](/Imagenes/Ejecución%20de%20programa.png)

    2. Desde un editor de código que contenga un interprete y una terminal. Ej: Visual Estudio Code
### Autor:
- Nombre y Apellido: Alejandro Rodriguez Salas
- Contancto: ale_rodra@live.com.ar
### Detalles:
* ##### Versión: 1.0 
* FECHA: 22/09/2020 
