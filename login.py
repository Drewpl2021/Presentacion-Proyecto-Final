from utiles import limpiarpantalla
import time
import getpass
from productos import productos 
def main():
    acumulador = 0
    while True and acumulador != 3:

        user = input("Ingrese Usuario: ")
        passwd = getpass.getpass("Ingrese password: ")

        if passwd == "123":
            limpiarpantalla()
            break
        else:
            print("Contraseña incorrecta")
            acumulador += 1
            time.sleep(2)
            limpiarpantalla(i) 
#---------------------------------------------------

