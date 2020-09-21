#!/usr/bin/env python
'''
Proyecto integrador de Python Inicial [Python]
Funciones de proyecto
---------------------------
Autor: Alejandro Rodriguez Salas
Version: 1.0

Descripcion:
Esta librería contiene modulos que serviran para 
la funcionalidad del proyecto
'''

__author__ = "Alejandro Rodriguez Salas"
__email__ = "ale_rodra@live.com.ar"

import csv
import traceback
import os


def validar_opciones(opcion,valores_validos):
    '''
    Dado una lista de valores dados ingresados por parametro\n
    se verifica si la opcion de entrada por parametro\n
    pertenece a la lista de valores validos\n
    Devuelve la opción perteneciente a la lista
    '''
    while True:
        if opcion in valores_validos: #Si es una opción valida la devuelve
            return opcion
        else: #Si no es una opción valida la vuelve a pedir
            print('Error! Opciones validas',valores_validos)
            opcion = str(input('Por favor, ingrese otra opcion:\n'))


def ingreso_de_menu(): #MENU PRINCIPAL
    '''
    Escribe el menu y devuelve la \n
    opción elegida
    '''
    
    print('''
    MENU:
    1_ Agregar nuevo cliente
    2_ Modificar/agregar datos de cliente existente
    3_ Eliminar cliente
    4_ Agregar producto
    5_ Modificar/agregar descripción de producto
    6_ Ingresar venta
    7_ Reporte de venta por cliente
    8_ Reporte de venta general
    9_ Salir del programa
    ''' )
    opcion = str(input('Opción: '))
    lista_opciones = ['1','2','3','4','5','6','7','8','9']

    opcion = validar_opciones(opcion=opcion,valores_validos=lista_opciones)
    
    return opcion


def validar_respuesta(respuesta):
    '''
    Valida la respuesta S o N y devuelve su estado natural
    S: True
    N: False
    '''
    while True: #Valida que La opción sea S o N
        if (respuesta == 'S' or respuesta == 's' or 
            respuesta == 'N' or respuesta == 'n'):
            break
        else:
            respuesta = str(input('Opción invalida, escriba su respues S/N: \n'))

    if respuesta == 's' or respuesta == 'S': #Devuelve el True si es Sí o devuelve False si es NO
        return True
    else:
        return False 


def ingresar_modificar_salir():
    '''
    Opciones a elegir si se quiere escribir en archivo\n
    o si se desea modificar algo o cancelar operación\n
    devuelve opcion elegida
    '''
    #Sub MENU dentro de las tareas elegidas del MENU principal
    print('''
    1_ Ingresar
    2_ Modificar datos 
    3_ Cancelar ingreso y volver al menu''')
    opcion = str(input('Opcion: '))
    opcion = validar_opciones(opcion=opcion,valores_validos=['1','2','3'])

    return opcion


def agregar_cliente(arch_clientes): #OPCIÓN 1: Agregar cliente
    '''
    agrega una nueva linea de datos de cliente\n
    al archivo que entra por parametro
    '''
    print('\n           AGREGAR CLIENTE\n')
    header = ['ID','Nombre y Apellido','Direccion','Telefono','Mail','Documento']
    agr_clint = csv.DictWriter(arch_clientes,fieldnames=header)
    with open('Clientes.csv') as fo:
        data = list(csv.DictReader(fo))
    
    if len(data) == 0: #Si el archivo no tiene lineas escribe el encabezado e inicializa el ID
        idd = 1
        agr_clint.writeheader()

    else:   #Le suma 1 al ultimo ID escrito en el archivo
        idd = int(data[len(data)-1].get('ID')) + 1

    campo = None

    while True:
        if campo == None or campo == 'a':
            nombre = str(input('Ingrese nombre y apellido del cliente: '))
        if campo == None or campo == 'b':
            dire = str(input('Ingrese dirección: '))
        if campo == None or campo == 'c':
            tel = str(input('Ingese teléfono: '))
        if campo == None or campo == 'd':
            mail = str(input('Ingrese mail: '))
        if campo == None or campo == 'e':
            doc = str(input('Ingrese documento: '))
            campo = None
            for i in range(len(data)):
                if doc == data[i].get('Documento'): #Verifica si ya hay otro cliente con el mismo documento
                    print('Documento ya existente')
                    resp = str(input('¿Desea cambiar el documento? S/N  '))
                    if validar_respuesta(respuesta=resp):
                        campo = 'e'
                    break
            if campo == 'e':
                continue
          
        opcion = ingresar_modificar_salir()

        if opcion == '1': #Ingreso de datos del cliente 
            print('''_Datos Cliente_
                ID: {}
                Nombre y Apellido: {}
                Dirección: {}
                Teléfono: {}
                Mail: {}
                Documento {}'''.format(idd,nombre,dire,tel,mail,doc))
            confirmacion = str(input('¿Seguro que desea ingresar estos datos? S/N\n'))
            if validar_respuesta(respuesta=confirmacion): #Confirmación
                agr_clint.writerow({
                    'ID': idd,
                    'Nombre y Apellido':nombre,
                    'Direccion':dire,
                    'Telefono':tel,
                    'Mail':mail,
                    'Documento':doc})
                arch_clientes.flush()
                print('\n**Datos ingresados con exito**\n')
            else:
                print('\n\nIngrese opcion 2 si desea cambiar algun dato')
                campo = False
                continue
            
            resp = str(input('Desea Ingresar otro cliente: S/N\n'))
            if validar_respuesta(respuesta=resp):
                idd += 1
                campo = None
                continue
            else:
                break 
        
        elif opcion == '2': #Modificacion de algún dato
            print('''\nIngrese el campo que desee modificar
            a_ Nombre y Apellido
            b_ Dirección
            c_ Teléfono
            d_ Mail
            e_ Documento''') 
            campo = str(input('campo:  '))
            lista_campos = ['a','b','c','d','e']
            campo = validar_opciones(opcion=campo,valores_validos=lista_campos)
        
        elif opcion == '3': #Volver al MENU
            break


def guardar_en_archivo_clientes(datos):
    '''
    Escribe en el archivo 'Cliente.csv' la lista que se ingrese\n
    como parametro, siempre y cuando tenga el mismo encabezado
    '''
    csvfo = open('Clientes.csv','w',newline='')
    header = ['ID','Nombre y Apellido','Direccion','Telefono','Mail','Documento']
    nuevo_archivo = csv.DictWriter(csvfo,fieldnames=header)
    nuevo_archivo.writeheader()
    
    for i in range(len(datos)):
        nuevo_archivo.writerow({
            'ID':datos[i].get('ID'),
            'Nombre y Apellido':datos[i].get('Nombre y Apellido'),
            'Direccion':datos[i].get('Direccion'),
            'Telefono':datos[i].get('Telefono'),
            'Mail':datos[i].get('Mail'),
            'Documento':datos[i].get('Documento')})
    csvfo.close()


def validar_indice(lista,indice,campo):
    '''
    Valida que, tanto ID como Codigo, que se pasa por parametro sea\n
    valido para la lista que tambien se pasa por parametro y\n
    devuelve el indice en el que se encuentra los datos
    '''
    while True: 
        for i in range(len(lista)): #Recorre la lista en busca de una coincidencia
            if indice == lista[i].get(campo):
                indice = i
                return indice
        # Si no encuentra una coincidencia en toda la lista quiere decir que no existe        
        print('Error! No se encuentra en el archivo')
        indice = str(input('Ingrese nuevo indice:  '))


def modificar_cliente(lista): #OPCIÓN 2: Modificar cliente
    '''
    Toma por parametros la lista diccionario en la cual se \n
    se realizaran los cambios y devuelve dicha lista modificada
    ''' 
    print('\n           MODIFICAR DATOS DE CLIENTE\n')
    ide = str(input('Ingrese el ID del cliente: '))
    indice = validar_indice(lista=lista,indice=ide,campo='ID')
    print('\nDatos actual\n',lista[indice])
    while True:
        lista_campos = ['Nombre y Apellido','Direccion','Telefono','Mail','Documento']
        print('\n',lista_campos)
        campo = str(input('¿Qué campo desea modificar?\n'))
        campo = validar_opciones(opcion=campo,valores_validos=lista_campos) #Procura que se ingrese bien el campo
        
        print('{} actual: {}'.format(campo,lista[indice].get(campo)))
        modificacion = str(input('Ingrese nuevo {}:   '.format(campo))) #Ingreso de nuevo dato
        
        resp = str(input('¿Esta seguro que desea realizar esta tarea?: S/N \n'))
        if validar_respuesta(respuesta=resp): #Confirmación de modificación
            lista[indice][campo] = modificacion
            print('**Moficación realizada**')        
        salida = str(input('\n¿Desea modificar otro campo?:  S/N\n'))
        if validar_respuesta(respuesta=salida):
            pass
        else: #Volver al MENU
            return lista


def eliminar_cliente(lista): #OPCIÓN 3: Eliminar cliente
    '''
    Función que elimina linea solicitada por el usuario\n
    y devuelve lista modificada
    '''
    print('\n           ELIMINACION DE CLIENTE\n')
    while True:
        ide = str(input('Ingrese el ID del cliente que desee borrar: '))
        linea = validar_indice(lista=lista,indice=ide,campo='ID')     # Verificar que exista el ID
        print('\nDatos actual\n',lista[linea])
        resp = str(input('\n¿Esta seguro que desea eliminar este cliente?: S/N\n'))
        if validar_respuesta(respuesta=resp): #Confirmar la eliminación del cliente ingresado
            lista.pop(linea)
            print('**Operación realizada con exito**\n')
        salida = str(input('¿Desea eliminar otro cliente?: S/N\n'))
        if validar_respuesta(respuesta=salida): #Volver a eliminar cliente
            pass
        else: #Volver al MENU con nueva lista
            return lista        


def agregar_producto(arch_producto): #OPCIÓN 4: Agregar producto
    '''
    agrega una nueva linea de datos de productos\n
    al archivo que entra por parametro
    '''
    print('\n           AGREGAR PRODUCTO\n')
    header = ['Codigo','Descripcion','Familia','Marca']
    linea_producto = csv.DictWriter(arch_producto,fieldnames=header)
    with open('Productos.csv') as fo:
        data = list(csv.DictReader(fo))

    if len(data) == 0: #Si no hay lineas en el archivo escribe el encabezado e inicializa el código
        cod = 101
        linea_producto.writeheader()

    else: #Le suma 1 al ultimo código escrito en el archivo
        cod = int(data[len(data)-1].get('Codigo')) + 1
   
    campo = None
    while True:  
        if campo == None or campo == 'a':
            descripcion = str(input('Ingrese Descrición del producto: '))
        if campo == None or campo == 'b':
            familia = str(input('Ingrese familia: '))
        if campo == None or campo == 'c':
            marca = str(input('Ingese marca: '))
        
        opcion = ingresar_modificar_salir() #Sub-MENU

        if opcion == '1': #Ingreso de producto
            print('''__Datos del producto__
                Descripcion: {}
                Familia: {}
                Marca: {}'''.format(descripcion,familia,marca))
            confirmacion = str(input('¿Seguro que desea ingresar estos datos? S/N\n'))
            if validar_respuesta(respuesta=confirmacion): #Confirmar
                linea_producto.writerow({
                    'Codigo': cod,
                    'Descripcion':descripcion,
                    'Familia':familia,
                    'Marca':marca})
                print('\n**Datos ingresados con exito**\n')
            else:
                print('\n\nIngrese opcion 2 si desea cambiar algun dato')
                campo = False
                continue
            resp = str(input('Desea Ingresar otro producto: S/N\n'))
            if validar_respuesta(respuesta=resp):
                cod += 1
                campo = None
            else:
                break
        
        if opcion == '2': #Modificacion de datos
            print('''Ingrese el campo que desee modificar
            a_ Descripcion
            b_ Familia
            c_ Marca''') 
            campo = str(input('campo:  '))
            lista_campos = ['a','b','c']
            campo = validar_opciones(opcion=campo,valores_validos=lista_campos)
        
        if opcion == '3': #Volver al MENU principal
            break


def guardar_en_archivo_productos(datos):
    '''
    Escribe en el archivo 'Productos.csv' la lista que se ingrese\n
    como parametro, siempre y cuando tenga el mismo encabezado
    '''
    csvfo = open('Productos.csv','w',newline='')
    header = ['Codigo','Descripcion','Familia','Marca']
    nuevo_archivo = csv.DictWriter(csvfo,fieldnames=header)
    nuevo_archivo.writeheader()
    
    for i in range(len(datos)):
        nuevo_archivo.writerow({
            'Codigo':datos[i].get('Codigo'),
            'Descripcion':datos[i].get('Descripcion'),
            'Familia':datos[i].get('Familia'),
            'Marca':datos[i].get('Marca')})
    csvfo.close()


def modificar_producto(lista): #OPCIÓN 5: Modificar producto
    '''
    Toma por parametros la lista diccionario en la cual se \n
    se realizaran los cambios y devuelve dicha lista modificada
    '''
    print('\n           MODIFICAR DATOS DE PRODUCTO\n')
    cod = str(input('Ingrese Codigo del producto: '))
    cod = validar_indice(lista=lista,indice=cod,campo='Codigo')
    while True:
        lista_campos = ['Descripcion','Familia','Marca']
        print(lista_campos)
        campo = str(input('¿Qué campo desea modificar?\n'))
        campo = validar_opciones(opcion=campo,valores_validos=lista_campos) #Verificar que el campo ingresado sea válido

        print('{} actual: {}'.format(campo,lista[cod].get(campo)))
        modificacion = str(input('Ingrese nuevo {}: \n'.format(campo))) #Ingreso de nuevo dato

        resp = str(input('¿Esta seguro que desea realizar esta tarea?: S/N \n'))
        if validar_respuesta(respuesta=resp): #Confirmacion de modificación
            lista[cod][campo] = modificacion
            print('**Moficación realizada con exito**')
        
        salida = str(input('¿Desea modificar otro campo?:  S/N\n'))
        if validar_respuesta(respuesta=salida): #Vuelve a modificar otro campo
            pass
        else: #Devuelve la lista modificada al Programa Principal
            return lista


def agregar_venta(lista_cliente,lista_producto,arch_ventas,flush_arch): #OPCIÓN 6: Ingreso de venta
    '''
    Analisa y manipula los datos de las listas de cliente y producto\n
    ingresada por parametro y escribe en un archivo las ventas realizadas
    '''
    print('\n           INGRESO DE VENTA\n')
    campo = None
    while True:
        if campo == None or campo == 'a': #Datos del cliente
            ide = str(input('ingrese el ID de cliente:  '))
            indice_cliente = validar_indice(lista=lista_cliente,indice=ide,campo='ID') #Verifica que exista el ID
            ide = lista_cliente[indice_cliente].get('ID')
            if lista_cliente[indice_cliente].get('Nombre y Apellido') != '': 
                cliente = lista_cliente[indice_cliente].get('Nombre y Apellido')
            else:
                cliente = None
                print('Nombre y apellido del cliente no encontrado\n')

        if campo == None or campo == 'b': #Datos del producto
            cod = str(input('\nIngrese el código del producto:  '))
            indice_producto = validar_indice(lista=lista_producto,indice=cod,campo='Codigo') #Verifica que exista el código ingresado
            cod = lista_producto[indice_cliente].get('Codigo')
            if lista_producto[indice_producto].get('Descripcion') != '':
                producto = lista_producto[indice_producto].get('Descripcion')
            else: 
                producto = None
                print('Descripción del producto no encontrado\n')

        if campo == None or campo == 'c':
            cantidad = int(input('\nIngrese la cantidad de {}:  '.format(producto)))

        if campo == None or campo == 'd':
            precio = float(input('\nIngrese el precio del producto - {}: $'.format(producto)))

        total_precio = precio * cantidad

        print('''Venta:
        Cliente: {}
        Producto: {}
        Cantidad: {}
        Precio: ${}
        
        TOTAL:$ {}'''.format(cliente,producto,cantidad,precio,total_precio))

        opcion = ingresar_modificar_salir()
        
        if opcion == '1': #Ingresar venta
            arch_ventas.writerow({
                'ID cliente': ide,
                'Nombre cliente': cliente,
                'Codigo de producto': cod,
                'Descripcion del producto': producto,
                'Cantidad': cantidad,
                'Precio $ (unidad)': precio,
                'TOTAL $': total_precio
            })
            flush_arch.flush()
            print('\n**Venta ingresada**')
            resp = str(input('¿Desea ingresar otra venta?:  S/N\n'))
            if validar_respuesta(respuesta=resp):
                campo = None
            else:
                break
        
        elif opcion == '2': #Modificar datos de venta
            print('''Ingrese el campo que desee modificar
            a_ Cliente
            b_ Producto
            c_ Cantidad
            d_ Precio
            ''') 
            campo = str(input('campo:  '))
            lista_campos = ['a','b','c','d']
            campo = validar_opciones(opcion=campo,valores_validos=lista_campos)

        elif opcion == '3': #Volver al MENU
            break 
          

def reporte_cliente(ventas,clientes): #OPCIÓN 7: Reporte de venta POR CLIENTE
    '''
    Reporte de venta de cierto cliente
    Se pide por parametro la lista de venta y la lista de cliente
    '''
    print('\n           REPORTE DE VENTA POR CLIENTE\n')
    while True:
        #Inicialización de variables!!
        total_max_precio = 0
        total_min_precio = 0
        acum = 0
        cont = 0
        lista_codigos = {'INICIALIZACION DE SET'}
        producto_cantidad = {}
        
        id_o_nombre = str(input('ingrese Nombre y apellido del cliente o su ID:  '))
        try: #Verifica si se ingreso una variable que pueda tranformarse en un numero entero
            ide = int(id_o_nombre)
            indice_cliente = validar_indice(lista=clientes,indice=id_o_nombre,campo='ID')
            nombre = clientes[indice_cliente].get('Nombre y Apellido')
            ide = clientes[indice_cliente].get('ID')
        except: #Si no se puede transformar se deduce que se ingreso un nombre
            nombre = id_o_nombre
            for i in range(len(ventas)):
                if ventas[i].get('Nombre cliente') == nombre:
                    ide = ventas[i].get('ID cliente')
                    break
            if i == len(ventas)-1:
                print('Nombre no encontrado en archivo')
                continue
        
        for i in range(len(ventas)): 
            if ventas[i].get('ID cliente') == ide:
                acum += float(ventas[i].get('TOTAL $'))                 # Acumula el total de venta que tiene ingresado el cliente por su ID
                cont += 1                                               #cuenta la cantidad
                lista_codigos.add(ventas[i].get('Codigo de producto'))  #Agrega el codigo en un set para guardar un registro del producto

        if cont == 0: #Si no hay compras realizadas por ese cliente vuelve al MENU
            print('El cliente {} no tiene compras realizadas'.format(nombre))
            input('Presione enter para continuar')
            break

        promedio = acum / cont
        
        for i in lista_codigos:  #Ingresa en un diccionario el codigo con la cantidad vendida
            if i != 'INICIALIZACION DE SET':
                cantidad = 0
                for j in range(len(ventas)):
                    if (i == ventas[j].get('Codigo de producto') and
                        ide == ventas[j].get('ID cliente')):
                        cantidad += int(ventas[j].get('Cantidad'))
                producto_cantidad[i] = cantidad

        producto_mas_consumo = max(zip(producto_cantidad.values(),producto_cantidad.keys()))
        cod_max = producto_mas_consumo[1]
        cant_max= producto_mas_consumo[0]

        producto_menos_consumo = min(zip(producto_cantidad.values(),producto_cantidad.keys()))
        cod_min = producto_menos_consumo[1]
        cant_min= producto_menos_consumo[0]

        for i in range(len(ventas)): #Guarda el código, la cantidad y el total de precio del producto más comprado
            if producto_mas_consumo[1] == ventas[i].get('Codigo de producto'):
                descripcion_max = ventas[i].get('Descripcion del producto')
                total_max_precio += float(ventas[i].get('TOTAL $'))
                
        for i in range(len(ventas)): #Guarda el código, la cantidad y el total de precio del producto menos comprado
            if producto_menos_consumo[1] == ventas[i].get('Codigo de producto'):
                descripcion_min = ventas[i].get('Descripcion del producto')
                total_min_precio += float(ventas[i].get('TOTAL $'))
        
        print('''\nReporte de cliente {}:
        Total de gasto: ${}
        Cantidad de visitas: {}
        Promedio de consumo de cada venta: ${}

        Producto más comprado: {}
            COD:{}  cantidad:{}  Total: ${}
        Producto menos comprado: {}
            COD:{}  cantidad: {} Total ${}
        '''.format(nombre,acum,cont,promedio,
        descripcion_max,cod_max,cant_max,total_max_precio,
        descripcion_min,cod_min,cant_min,total_min_precio))    

        resp = str(input('¿Desea ver el reporte de otro cliente? S/N \n'))
        if validar_respuesta(respuesta=resp): #Vuelve al inicio
            pass
        else: #Vuelve al MENU
            break
          
            
def reporte_venta(ventas): #OPCIÓN 8: REPORTE DE VENTA GENERAL
    '''
    Reporte de venta general dado la lista de venta\n
    que ingresa por parametro
    '''
    print('\n       REPORTE DE VENTA GENERAL\n')
    #Inicialización de variables
    total_max_precio = 0
    total_min_precio = 0
    lista_codigos = {'INICIALIZACION DE SET'}
    acum = 0

    for i in range(len(ventas)):
        lista_codigos.add(ventas[i].get('Codigo de producto'))
        acum += float(ventas[i].get('TOTAL $'))
    
    promedio = acum / len(ventas)
    
    for i in lista_codigos:
            cantidad = 0
            for j in range(len(ventas)):
                if i == ventas[j].get('Codigo de producto'):
                    cantidad += int(ventas[j].get('Cantidad'))
                if i != 'INICIALIZACION DE SET':
                    producto_cantidad = {i:cantidad}
    
    producto_mas_consumo = max(zip(producto_cantidad.keys(),producto_cantidad.values()))
    cod_max = producto_mas_consumo[0]
    cant_max = producto_mas_consumo[1]

    producto_menos_consumo = min(zip(producto_cantidad.keys(),producto_cantidad.values()))
    cod_min = producto_menos_consumo[0]
    cant_min= producto_menos_consumo[1]

    for i in range(len(ventas)):
        if producto_mas_consumo[0] == ventas[i].get('Codigo de producto'):
            descripcion_max = ventas[i].get('Descripcion del producto')
            total_max_precio += float(ventas[i].get('TOTAL $'))
    for i in range(len(ventas)):    
        if producto_menos_consumo[0] == ventas[i].get('Codigo de producto'):
            descripcion_min = ventas[i].get('Descripcion del producto')
            total_min_precio += float(ventas[i].get('TOTAL $'))

    print('''\n     REPORTE DE VENTA
    Total de ingreso: ${}
    cantidad de ventas: {}
    Promedio de consumo por cliente: ${}

    Producto más consumido: {}
        COD:{}  cantidad:{}  Total: ${}
    Producto menos consumido: {}
        COD:{}  cantidad: {} Total: ${}
    '''.format(acum,len(ventas),promedio,descripcion_max,cod_max,
    cant_max,total_max_precio,descripcion_min,cod_min,cant_min,total_min_precio))
    input('\nPresione enter para vovler al menu\n')