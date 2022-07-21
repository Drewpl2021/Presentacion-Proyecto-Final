import time
from funciones import Producto
from utiles import limpiarpantalla
ruta_archivo = "./productos/productos.txt"
#-------------------------------------------------------
def leer():
    with open("./productos/productos.txt", "r") as d:
        for linea in d:
            leer= linea
            print(f"{leer}\n")
#-------------------------------------------------------
def buscar(codigo):
    sapatilla = None 
    archivoSapatilla = open(ruta_archivo, "r")
    for linea in archivoSapatilla.readlines():
        atributos = linea.split(";")
        if codigo == atributos[0]:
            sapatilla = Producto(atributos[0],atributos[1],atributos[2],atributos[3],atributos[4],atributos[5])        
            break
    archivoSapatilla.close()
    return sapatilla
#-------------------------------------------------------
def agregar():
    codigo = input("Codigo: ")
    marca = input("Marca: ")
    color = input("Color: ")
    talla = input("Talla: ")
    genero = input("Genero: ")
    precio = input("Precio: S/. ")
    datos = Producto(codigo, marca, color, talla, genero, precio)
    archivoSapatilla = open(ruta_archivo, "a")
    archivoSapatilla.write(str(datos))
    archivoSapatilla.close()
#-------------------------------------------------------
def modificar_dato(ruta_archivo, filas, columna, nuevo_dato):
    contenido = list()
    with open(ruta_archivo, "r+") as archivo:
        contenido = archivo.readlines()
        for fila in filas:
            columnas = contenido[fila - 1].split(";")
            columnas[columna] = nuevo_dato
            contenido[fila - 1] = ";".join(columnas) + "\n"
    with open(ruta_archivo, "w") as archivo:
        archivo.writelines(contenido)
        limpiarpantalla()
        return print("Cambiado correctamente")
#-------------------------------------------------------
def productos():
    limpiarpantalla()
    while True:
        print("_________________________________")
        print("|        MENU DE PRODUCTOS       |")
        print(" ================================")
        print("|[1] Lista de productos          |")
        print("|[2] Agregar producto            |")
        print("|[3] Busacar producto            |")
        print("|[4] Editar precio del producto  |")
        print("|[0] Volver                      |")
        print("|________________________________|")     
        op=input()
        match (op):
            case "1":
                limpiarpantalla()
                print("------------------------------------")
                leer()
                print("------------------------------------")
                time.sleep(5)
                limpiarpantalla()
            case "2":
                limpiarpantalla()
                agregar()
                limpiarpantalla()
                print("Creado Correctamente!!!")
                time.sleep(3)
                limpiarpantalla()
            case "3":
                limpiarpantalla()
                codigo = input("Ingrese codigo de la sapatilla: ")
                fila = str(buscar(codigo))
                encontrado = fila.split(";")
                limpiarpantalla()
                print(encontrado)
                time.sleep(3)
                limpiarpantalla()
            case "4":
                limpiarpantalla()
                filas = int(input("Ingrese fila de la sapatilla: "))
                columna = int(5)
                nuevo_dato = input("Ingrese el nuevo precio: ")
                fila = str(modificar_dato(ruta_archivo, [filas], columna, nuevo_dato))
                encontrado = fila.split(";")
                time.sleep(3)
                limpiarpantalla()
            case "0":
                limpiarpantalla()
                print("REGRESANDO AL MENÚ PRINCIPAL")
                time.sleep(2)
                limpiarpantalla()
                break
            case _:
                print("La opcion que selecciono es invalida, por favor intentelo de nuevo")
