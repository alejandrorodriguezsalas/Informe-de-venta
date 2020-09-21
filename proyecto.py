#!/usr/bin/env python
'''
Proyecto integrador de Python Inicial [Python]
Reporte de venta por cliente
---------------------------
Autor: Alejandro Rodriguez Salas
Version: 1.0

Descripcion:
Mi proyecto se trata de almacenar datos de cada cliente
y de cada productos, para asi poder vincular ambos datos
en lo que se refiere a venta y poder hacer reportes de la
misma, ya sea por cliente como reportes de venta general
'''

__author__ = "Alejandro Rodriguez Salas"
__email__ = "ale_rodra@live.com.ar"
__version__ = "1.0"

import csv
import funciones_alejandro as ale
import os




if __name__ == '__main__':
    while True:
        opc = ale.ingreso_de_menu()
        if opc == '1': #Agregar cliente
            csvfile = open('Clientes.csv', 'a', newline='')
            ale.agregar_cliente(arch_clientes=csvfile)
            csvfile.close()
            continue
            
        elif opc == '2': #Modificar cliente
            if os.access('Clientes.csv',os.F_OK) is True:
                with open('Clientes.csv') as csvfile:
                    data = list(csv.DictReader(csvfile))
            else:
                print('''No se encuentra archivo
                Ingrese opcion 1 para crear archivo de clientes''')
                input('Ingrese enter para continuar')
                continue
            nueva_data = ale.modificar_cliente(lista=data)
            ale.guardar_en_archivo_clientes(datos=nueva_data)
            continue  

        elif opc == '3': #Eliminar cliente
            if os.access('Clientes.csv',os.F_OK) is True:
                with open('Clientes.csv') as csvfile:
                  clientes = list(csv.DictReader(csvfile)) 
            else:
                print('''No se encuentra archivo
                Ingrese opcion 1 para crear archivo de clientes''')
                input('Ingrese enter para continuar')
                continue
            clientes_nuevo = ale.eliminar_cliente(lista=clientes)
            ale.guardar_en_archivo_clientes(datos=clientes_nuevo)
            continue
                    
        elif opc == '4': #Agregar Producto
            csvfile = open('Productos.csv','a',newline='')   
            ale.agregar_producto(arch_producto=csvfile)
            csvfile.close()
            continue
        
        elif opc == '5': #Modificar Producto
            if os.access('Productos.csv',os.F_OK) is True:
                with open('Productos.csv') as csvfile:
                    data = list(csv.DictReader(csvfile))
            else:
                print('''No se encuentra archivo
                Ingrese opcion 4 para crear archivo de productos''')
                input('Ingrese enter para continuar')
                continue

            data_modificado = ale.modificar_producto(lista=data)
            ale.guardar_en_archivo_productos(datos=data_modificado)
            continue
        
        elif opc == '6': #Ingresar venta
            if os.access('Clientes.csv',os.F_OK) is True:
                with open('Clientes.csv') as csvfile_clientes:
                    data_clientes = list(csv.DictReader(csvfile_clientes))
            else:
                print('''No se encuentra archivo
                Ingrese opcion 1 para crear archivo de clientes''')
                input('Ingrese enter para continuar')
                continue
            
            if os.access('Productos.csv',os.F_OK) is True:
                with open('Productos.csv') as csvfile_productos:
                    data_productos = list(csv.DictReader(csvfile_productos))
            else:
                print('''No se encuentra archivo
                Ingrese opcion 4 para crear archivo de productos''')
                input('Ingrese enter para continuar')
                continue

            if os.access('Ventas.csv',os.F_OK) is True:
                csvfile_ventas = open('Ventas.csv','a',newline='')
                header = ['ID cliente','Nombre cliente','Codigo de producto','Descripcion del producto','Cantidad','Precio $ (unidad)','TOTAL $']
                data_ventas = csv.DictWriter(csvfile_ventas,fieldnames=header)
            else:
                csvfile_ventas = open('Ventas.csv','a',newline='')
                header = ['ID cliente','Nombre cliente','Codigo de producto','Descripcion del producto','Cantidad','Precio $ (unidad)','TOTAL $']
                data_ventas = csv.DictWriter(csvfile_ventas,fieldnames=header)
                data_ventas.writeheader()
            ale.agregar_venta(lista_cliente=data_clientes,lista_producto=data_productos,arch_ventas=data_ventas,flush_arch=csvfile_ventas)
            csvfile_ventas.close()
            continue
        
        elif opc == '7': #Reporte de venta por cliente
            if os.access('Clientes.csv',os.F_OK) is True:
                with open('Clientes.csv') as csvfile_clientes:
                    data_clientes = list(csv.DictReader(csvfile_clientes))
            else:
                print('''No se encuentra archivo
                Ingrese opcion 1 para crear archivo''')
                input('Ingrese enter para continuar')
                continue
        
            if os.access('Ventas.csv',os.F_OK) is True:
                with open('Ventas.csv') as csvfile_ventas:
                    data_ventas = list(csv.DictReader(csvfile_ventas))
            else:
                print('''No se encuentra archivo
                Ingrese opcion 6 para crear archivo''')
                input('Ingrese enter para continuar')
                continue

            ale.reporte_cliente(ventas=data_ventas,clientes=data_clientes)
            continue
            
        elif opc == '8': #Reporte de venta general
            if os.access('Ventas.csv',os.F_OK) is True:
                with open('Ventas.csv') as csvfile:
                    data = list(csv.DictReader(csvfile))
            else:
                print('''No se encuentra archivo
                Ingrese opcion 6 para crear archivo''')
                input('Ingrese enter para continuar')
                continue

            ale.reporte_venta(ventas=data)
            continue
    
        elif opc == '9': #Salir
            print('***************************** FIN DEL PROGRAMA *****************************')
            break
        




        
