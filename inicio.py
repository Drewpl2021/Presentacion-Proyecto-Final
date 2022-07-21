from productos import productos
from login import main
from clientes import gestionClientes
from comprobante import comprobante
from utiles import limpiarpantalla
def inicio():
    main()
    while True:
        print(chr(27)+"[1;33m"+" ")
        print("____________________________")
        print("|      MENU DE INICIO      |")
        print(" ==========================")
        print("|[1] Ventas                |")
        print("|[2] Gestion de usuarios   |")
        print("|[3] Productos             |")
        print("|[0] Salir                 |")
        print("|__________________________|")
        print("Seleccione una opcion")
        op = input()
        match(op):
            case "1":
                limpiarpantalla()
                comprobante()
                limpiarpantalla()
            case "2":
                limpiarpantalla()
                gestionClientes()
                limpiarpantalla()
            case "3":
                limpiarpantalla()
                productos()
                limpiarpantalla()
            case "0":
                limpiarpantalla()
                print("HASTA PRONTO")
                time.sleep(3)
                limpiarpantalla()
                break
            case _:
                limpiarpantalla()
                print("Opcion invalida")
                time.sleep(2)
                limpiarpantalla()

inicio()

