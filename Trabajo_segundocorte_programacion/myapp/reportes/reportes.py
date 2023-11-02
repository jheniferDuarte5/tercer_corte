import os;
from reservas.reservas import reservas,canchas,historial_reservas;
from usuarios.usuarios import clientes;


def menu_reportes():
    os.system("cls")
    while True:
        print("Menú de Reportes")
        print("1. Ver Canchas")
        print("2. Ver Ingresos Totales de Dinero")
        print("3. Ver Reservas por Cliente")
        print("0. Volver al menú principal")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            mostrar_canchas_apartadas()
        elif opcion == "2":
            generar_reporte_ingresos()
        elif opcion == "3":
            generar_reporte_reservas_por_cliente()
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")



def generar_reporte_ingresos():
  os.system("cls");
  total = 0;
  for reserva in historial_reservas:
      total+=reserva[0];
  print(f"El total de ganancias es: {total}");
  

def generar_reporte_reservas_por_cliente():
    os.system("cls");
    print("=== Reporte de Reservas por Cliente ===")
    
    if not reservas:
        print("No se han registrado reservas.")
        return
    
    cedulas_clientes = set([cliente[0] for cliente in clientes])
    
    for cedula in cedulas_clientes:
        print("Reservas realizadas:")
        print("Cédula del Cliente:", cedula)
        for reserva in reservas:
            cliente = reserva[1]
            if cliente[0] == cedula:
                print(f"Dia: {reserva[3]}, Hora: {reserva[5]}, Cancha: {reserva[4]+1}, Precio: {reserva[0]}")
        # precio_base,cliente_encontrado, administrador_encontrado, fecha, cancha
        print("-----------------------------")

def mostrar_canchas_apartadas():
    os.system("cls");
    for cancha in canchas:
        if cancha[0] == 0:
            print(f"{cancha[1]:} Disponible")
        elif cancha[0] == 1:
            print(f"{cancha[1]:} Ocupada")    

