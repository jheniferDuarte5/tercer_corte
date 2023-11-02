# para reservar el cliente debe estar totalmente registrado
reservas = []
historial_reservas = [];
canchas = [[0,"Cancha 1"],[0,"Cancha 2"],[0,"Cancha 3"]]



import os
from os import system
from usuarios.usuarios import clientes,administradores,verificarClienteExiste;
from reportes.reportes import generar_reporte_reservas_por_cliente;

def gestionar_reservas():
    os.system("cls")
    while True:
        print("Gestión de Reservas")
        print("1. Realizar Reserva")
        print("2. Cancelar Reserva")
        print("0. Volver al menú principal")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            realizar_reserva()
        elif opcion == "2":
            cancelar_reserva();
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def cancelar_reserva():
    os.system("cls")
    print("Ingrese su la cèdula del cliente para cancelar la reserva")
    ced = input();
    reserva_existe=False;

    if verificarClienteExiste(ced) == False:
      print(f"No se encontraron reservas para el cliente con cédula {ced}.")
    else:
      for reserva in reservas:
          #puede haber 0 1 o
          cancha_eliminar = reserva[4]
          canchas[cancha_eliminar][0] = 0 
          reservas.remove(reserva)
          for hreserva in historial_reservas:
              if hreserva[1] == ced:
                  historial_reservas.remove(hreserva);
      print(f"Se eliminaron todas las reservas del cliente con cédula {ced}.")

# Método para realizar una reserva
def realizar_reserva():
    os.system("cls")
    print("Realizar Reserva")
    
    # Solicitar la cédula del cliente que realizará la reserva
    cedula_cliente = input("Ingrese la cédula del cliente: ")
    
    # Verificar si la cédula corresponde a un cliente registrado
    cliente_encontrado = False;
    for cliente in clientes:
        if cliente[0] == cedula_cliente:  # Comparamos con la cédula del cliente
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado == False:
        print("Cliente no encontrado. Verifique la cédula.")
        return
    
    # Solicitar la cédula del administrador que registra la reserva
    cedula_administrador = input("Ingrese la cédula del administrador: ")
    
    # Verificar si la cédula corresponde a un administrador registrado
    administrador_encontrado = False;
    for admin in administradores:
        if admin[0] == cedula_administrador:  # Comparamos con la cédula del administrador
            administrador_encontrado = admin
            break
    
    if administrador_encontrado == False:
        print("Administrador no encontrado. Verifique la cédula.")
        return

    # Solicitar detalles de la reserva
    precio_base = 40000
    
    
    fecha = input("Ingrese el dia de la semana de la reserva (sin tildes): ")
    hora = input("ingrese la hora de la reserva: ")
    if "miercoles" in fecha.lower():
          precio_base = precio_base * 0.85
    for cancha in canchas:
        if cancha[0] == 0:
            print(f"{cancha[1]} Disponible")
        elif cancha[0] == 1:
            print(f"{cancha[1]} Ocupada")

    while True:
      cancha_reservar = input("Ingrese la cancha a reservar ('s' para salir): ");
      hayDisponibles = True;
      if(cancha_reservar.isnumeric()):
          cancha_reservar = int(cancha_reservar) - 1;
          for cancha in canchas:
            if cancha[0] == 0:          
                pass;
      else:
          break;
      
      if(hayDisponibles == True):
        if(canchas[cancha_reservar][0] == 0):
            canchas[cancha_reservar][0] = 1;
            break;
        elif(cancha[cancha_reservar][0] == 1):
            print("Cancha ocupada, elija otra")
            pass;
      else:
        break;
          


    # Registrar la reserva con cliente y administrador
    nueva_reserva = [precio_base,cliente_encontrado, administrador_encontrado, fecha, cancha_reservar,hora,arbitro]
    reservas.append(nueva_reserva)
    historial_reservas.append(nueva_reserva);
    print("Reserva realizada con éxito.")


