import os;
#declaramos las listas de los usuarios
clientes = []
administradores = [["1065873757","Andrea","Duarte","Administrador","3129831298","Carrera 45"]]
arbitros = [["1003041683","Didier","Elprofe"]]


def verificarClienteExiste(cedula):
  for cliente in clientes:
      if cliente[0] == cedula:
       return True;
  return False;

def verificarAdminExiste(cedula):
  for cliente in clientes:
      if cliente[0] == cedula:
       return True;
  return False;

def agregar_cliente():
    # pedimos los datos necesarios para agregar cliente
    ced = input("Ingrese la cédula del cliente: ")
    if(verificarClienteExiste(ced)==True):
       print("Ese cliente ya existe.")
       return;
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    direccion = input("Ingrese el direccion electrónico del cliente: ")
    nuevo_cliente = [ced,nombre, apellido, "Cliente", telefono, direccion,]
    clientes.append(nuevo_cliente)
    print("Cliente agregado con éxito.")

def agregar_administrador():
    ced = input("Ingrese la cédula del administrador: ")
    if(verificarAdminExiste(ced)==True):
       print("Ese administrador ya existe.")
       return;
    nombre = input("Ingrese el nombre del administrador: ")
    apellido = input("Ingrese el apellido del administrador: ")
    telefono = input("Ingrese el teléfono del administrador: ")
    direccion = input("Ingrese la dirección del administrador: ")
    nuevo_administrador = [ced,nombre, apellido, "Administrador",telefono,direccion]

    administradores.append(nuevo_administrador)
    print("Administrador agregado con éxito.")

def agregar_arbitro():
  ced = input("Ingrese la cédula del arbitro")
  nombre = input("Ingrese el nombre del cliente: ")
  apellido = input("Ingrese el apellido del cliente: ")
  arbitros.append([ced,nombre,apellido])
# Método para realizar una reserva


def gestionar_usuarios():
  # esto es para limpiar la consola no se les olvide porfa
    os.system("cls")
    while True:
        print("Gestión de Usuarios")
        print("1. Agregar Cliente")
        print("2. Agregar Administrador")
        print("3. Listar Clientes")
        print("4. Listar Administradores")
        print("5. Listar Arbitros")
        print(". Volver al menú principal")
        opcion = input("Elija una opción: ")
        os.system("cls")
        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            agregar_administrador()
        elif opcion == "3":
           ver_clientes();
        elif opcion == "4":
            ver_administradores();
        elif opcion == "5":
           ver_arbitros();
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def ver_clientes():
  for cliente in clientes:
     print(f"{cliente[1]} {cliente[2]}, Telefono: {cliente[4]}, Direccion: {cliente[5]}")

def ver_administradores():
  for admin in administradores:
     print(f"{admin[1]} {admin[2]}, Telefono: {admin[4]}, Direccion: {admin[5]}")

def ver_arbitros():
  for arb in arbitros:
     print(f"{arb[1]} {arb[2]}, Cedula: {arb[0]}")