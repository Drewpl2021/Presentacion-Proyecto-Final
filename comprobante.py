from  utiles import limpiarpantalla
import time
from main import Comprobante, Clientes, Clientes2
from funciones import Producto, Productos2
ruta_archivo = "./archivos/comprobante.txt"
ruta_clientes = "./archivos/clientes.txt"
ruta_productos = "./productos/productos.txt"
def lista():
    with open("./archivos/comprobante.txt", "r") as d:
        for linea in d:
            leer= linea
            print(f"{leer}\n")
#-------------------------------------------------------
def nombreapellido(dni):
    nombreapellidos = None
    cliente = open(ruta_clientes, "r")
    for linea in cliente.readlines():
        atributos = linea.split(";")
        if dni == atributos[0]:
            nombreapellidos = Clientes2(atributos[1])        
            break
    cliente.close()
    return nombreapellidos

#----------------------------------------------------------------------------------
def buscar_precio(codigo_producto):
    precioP= None
    archivoC = open(ruta_productos, "r")
    for linea in archivoC.readlines():
        atributos = linea.split(";")
        if codigo_producto == atributos[0]:
            precioP = Productos2(atributos[5])        
            break
    archivoC.close()
    return precioP
#--------------------------------------------------
def Crear_comprobante():
    ruc = input("Ingrese el RUC del comprobante: ")
    dni= input("Ingrese DNI: ")
    fila = str(nombreapellido(dni))
    nombre_apellidos = fila.split(";")
    print(nombre_apellidos)

    fecha = input("Ingrese la fecha: ")
    codigo_producto= input("Ingrese el codigo del producto: ")
    cantidad_de_producto=input("Ingrese la cantidas de productos de venta: ")
    fila = str( buscar_precio(codigo_producto))
    precio = fila.split(";")
    print(precio)
#----------------------------------------------------------------------
    total = 1
    comprobante = Comprobante(ruc, dni, nombre_apellidos, fecha,codigo_producto, cantidad_de_producto, precio, total)
    archivoComprobante = open(ruta_archivo, "a")
    archivoComprobante.write(str(comprobante))
    archivoComprobante.close() 
    print("============================================================")
    print("|                     COMPROBANTE DE PAGO                  |")
    print("------------------------------------------------------------")
    print(f"| Ruc del comprobante:{ruc}                                   |")
    print(f"| DNI:{dni}                                             |")
    print(f"| Nombres y apellidos:{nombre_apellidos}              |")
    print(f"| Fecha:{fecha}                                         |")
    print(f"| Codigo del producto:{codigo_producto}                                   |")
    print(f"| cantidas de productos de venta:{cantidad_de_producto}                         |")
    print(f"| precio:{precio}                                        |")
    print("------------------------------------------------------------")
#-----------------------------------------------------------------------------
def Editar_comprobante(ruta_archivo, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta_archivo, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(contenido)
        return print("Cambiado correctamente")
#-------------------------------------------------------

def buscar_comprobante(ruc):
    comprobante = None 
    archivoComprobante = open(ruta_archivo, "r")
    for linea in archivoComprobante.readlines():
        atributos = linea.split(";")
        if ruc == atributos[0]:
            comprobante = Producto(atributos[0],atributos[1],atributos[2],atributos[3],atributos[4],atributos[5])        
            break
    archivoComprobante.close()
    return comprobante
#-------------------------------------------------------


def comprobante():
    while True:
        print("============================")
        print(" MENÚ DE VENTAS ")
        print("============================")
        print("1. Lista de comprobante")
        print("2. Crear comprobante")
        print("3. Editar comprobante")
        print("4. Buscar comprobante")
        print("0. Salir")
        op = int(input("Opción: "))

        match (op):
            case 1:
                limpiarpantalla()
                lista()

            case 2:
                limpiarpantalla()
                Crear_comprobante()

            case 3:
                print("Menu de modificar dato")
                print("1. RUC")
                print("2. DNI")
                print("3. Nombre y apellido ")
                print("4. Fecha ")
                print("5. Codigo de producto")
                print("6. Cantidad del producto ")
                print("7. Costo del producto")
                print("0. Volver")               
                op = input("Ingrese una opcion:")
                match(op):
                    case "1":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(0)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas],           columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "2":
                        filas = int(input("Ingrese fila del cambio: "))
                        columna = int(1)
                        nuevo_dato = input("Ingrese el nuevo dato ")
                        fila = str(modificar_dato(ruta_archivo, [filas],           columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "3":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(2)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas],columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "4":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(3)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas],          columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)

                    case "5":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(4)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas],          columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)

                    case "6":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(5)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas],          columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)

                    case "7":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(6)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas],          columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)

                    case "0":
                        pass
                    case _:
                        print("Opcion incorrecta")
            case 4:
                limpiarpantalla()
                ruc = input("Ingrese el RUC del comprobante: ")
                fila = str(buscar_comprobante(ruc))
                encontrado = fila.split(";")
                print(encontrado)


            case 0:
                limpiarpantalla()
                print("Saliendo del sistema... hasta pronto")
                break

            case _:
                print("opción incorrecta")
                time.sleep(2)
                limpiarPantalla()
