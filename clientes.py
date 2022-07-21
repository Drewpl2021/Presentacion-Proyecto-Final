from funciones import Clientes
from utiles import limpiarpantalla
import time
ruta_archivo = "./archivos/clientes.txt"
#------------------------------------------------------------
def crearCliente():
    Dni = input("Identificacion: ")
    nombres_apellidos = input("Nombres y Apellidos: ")
    direccion = input("Dirección: ")
    telefono = input("Telefono: ")
    email = input("Correo Electronico: ")

    Cliente = Clientes(Dni, nombres_apellidos, direccion, telefono, email)

    archivoCliente = open(ruta_archivo, "a")
    archivoCliente.write(str(Cliente))
    archivoCliente.close()
#--------------------------------------------------------------
def lista():
    with open("./archivos/clientes.txt","r") as d:
        for linea in d:
            lista = linea
            print(f'{lista}\n')

#---------------------------------------------------------------
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
        return print("Cambiado Correctamente")
#--------------------------------------------------------------
def gestionClientes():
    while True:
        print("_______________________________")
        print("| MENU DE GESTION DE CLIENTES |")
        print("|=============================|")
        print("|[1] Crear Cliente            |")
        print("|[2] Lista de Cliente         |")
        print("|[3] Editar Cliente           |")
        print("|[4] Buscar Cliente           |")
        print("|[0] Volver                   |")
        print("|_____________________________|")
        op = input("Ingrese una opcion: ")
        match (op):
            case "1":
                print("Esta apunto de crear un nuevo usuario")
                limpiarpantalla()
                crearCliente()
            case "2":
                limpiarpantalla()
                print("--------------------------------------------------")
                lista()
                print("--------------------------------------------------")
            case "3":
                print("Menu de modificar dato")
                print("1. Dirrecion")
                print("2. Telefono")
                print("3. Correo Electronico")
                print("0. Volver")
                op = input("Ingrese una opcion:")

                match(op):
                    case "1":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(2)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas], columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "2":
                        filas = int(input("Ingrese fila del cambio: "))
                        columna = int(3)
                        nuevo_dato = input("Ingrese el nuevo dato ")
                        fila = str(modificar_dato(ruta_archivo, [filas], columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "3":
                        filas = int(input("Ingrese la fila: "))
                        columna = int(4)
                        nuevo_dato = input("Ingrese el nuevo dato: ")
                        fila = str(modificar_dato(ruta_archivo, [filas], columna, nuevo_dato))
                        encontrado = fila.split(";")
                        print(encontrado)
                    case "0":
                        pass
                    case _:
                        print("Opcion incorrecta")

            case "0":
                break
            case _:
                print("Obcion invalida")
