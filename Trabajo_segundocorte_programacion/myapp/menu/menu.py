#importamos system del paquete os para mas adelante poder 
# limpiar la consola
from os import system
#importamos los menus
from usuarios.usuarios import gestionar_usuarios;
from reservas.reservas import gestionar_reservas,reservas;
from reportes.reportes import menu_reportes;




#mostramos el menu principal
def mostrarMenuPrincipal():
  while True:
        print("      MENU PRINCIPAL     ")
        print("-------------------------")
        print("1. GESTION DE USUARIOS   ")
        print("2. GESTION DE RESERVAS   ")
        print("3. GESTION DE REPORTES   ")
        print("0. SALIR                 ")
        print("-------------------------")
        opcion = input("Ingrese una opción: ")
        if opcion == "0":
            print("Saliendo de la aplicación...")
            break;
        if opcion == '1':
            gestionar_usuarios();
        elif opcion == '2':
            gestionar_reservas();
        elif opcion == '3':
            menu_reportes();
        else:
            print("Opción no válida. Por favor, elige una opción válida.")