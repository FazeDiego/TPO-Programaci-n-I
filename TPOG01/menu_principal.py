from os import system
from time import sleep
from funciones_paciente import *
from funciones_turno import *
from adicionales import *

limpiar_consola = lambda: system("cls")


def menu():
    dnis_activos = enlistar_columna_fichero("Pacientes", 0)
    continuar = True
    while continuar:
        limpiar_consola()
        titulo()
        print(" PACIENTES\n"
              " 1) Alta paciente\n"
              " 2) Baja paciente\n"
              " 3) Modificar paciente\n"
              " 4) Mostrar pacientes\n"
              " TURNOS\n"
              " 5) Alta turno\n"
              " 6) Baja turno\n"
              " 7) Modificar turno\n"
              " 8) Mostrar turnos\n"
              " 9) Turnos del dia\n"
              " 0) Salir")

        opcion_elegida = ingresar_opcion("..: ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        print()  # Salto de linea.
        limpiar_consola()

        # PACIENTES
        if opcion_elegida == 1:  # Alta paciente
            dni_objetivo = ingresar_dni("Ingrese DNI del paciente: ")
            if not str(dni_objetivo) in dnis_activos:
                alta_paciente("Pacientes", dni_objetivo)
                print("Paciente agregado con exito!")
                dnis_activos.append(str(dni_objetivo))
                sleep(2)
            else:
                print("El paciente ya se encuentra registrado!")
                sleep(2)
        if opcion_elegida == 2:  # Baja paciente
            dni_objetivo = ingresar_dni("Ingrese DNI del paciente que desea dar de baja: ")
            if str(dni_objetivo) in dnis_activos:
                baja_paciente("Pacientes", dni_objetivo)
                baja_turno("Turnos", dni_objetivo)
                print("Paciente dado de baja con exito!")
                eliminar_valor(dnis_activos, str(dni_objetivo))
                sleep(2)
            else:
                print("Error: el paciente no existe!")
                sleep(2)
        if opcion_elegida == 3:  # Modificar paciente
            dni_objetivo = ingresar_dni("Ingrese DNI del paciente que desea modificar: ")
            if existe_paciente("Pacientes", dni_objetivo):
                modificar_paciente("Pacientes", dni_objetivo)
                print("Paciente modificado con exito!")
                sleep(2)
            else:
                print("Error: el paciente no existe!")
                sleep(2)
        if opcion_elegida == 4:  # Mostrar pacientes
            mostrar_pacientes("Pacientes")
            print("1) Ordenar por nombre\n"
                  "2) Ordenar por edad\n"
                  "3) Filtrar por edad\n"
                  "0) Volver")
            seleccion = ingresar_opcion("..: ", [1, 2, 3, 0])
            if seleccion == 1:  # Ordenar por nombre
                limpiar_consola()
                ordenar_por_nombre("Pacientes")
                mostrar_pacientes("Pacientes")
                print("0) Volver")
                seleccion = ingresar_opcion("..: ", [0])
            if seleccion == 2:  # Ordenar por edad
                limpiar_consola()
                ordenar_por_edad("Pacientes")
                mostrar_pacientes("Pacientes")
                print("0) Volver")
                seleccion = ingresar_opcion("..: ", [0])
            if seleccion == 3:  # Filtrar por edad
                limpiar_consola()
                mayor_igual = int(input("Mayor o igual a: "))
                filtrar_por_edad(mayor_igual, "Pacientes")
                print("0) Volver")
                seleccion = ingresar_opcion("..: ", [0])
            if seleccion == 0:  # Volver
                limpiar_consola()
                pass

        # TURNOS
        fechas_ocupadas = enlistar_listas("Turnos", 0, 4)
        fechas_ocupadas_sin_dni = [f[1:] for f in fechas_ocupadas]

        if opcion_elegida == 5:  # Alta turno
            dni_objetivo = ingresar_dni("Ingrese DNI del paciente: ")
            if existe_paciente("Pacientes", dni_objetivo):
                if not existe_turno_asignado("Turnos", dni_objetivo):
                    alta_turno("Turnos", dni_objetivo, fechas_ocupadas_sin_dni)
                    print("Turno agregado con exito!")
                    sleep(2)
                else:
                    print("Error: el paciente ya posee un turno asignado!")
                    sleep(2)
            else:
                print("Error: el paciente no existe!\n"
                      "Agreguelo para poder asignarle un turno.")
                sleep(2)
        if opcion_elegida == 6:  # Baja turno
            dni_objetivo = ingresar_dni("Ingrese DNI del paciente asociado al turno: ")
            if existe_turno_asignado("Turnos", dni_objetivo):
                baja_turno("Turnos", dni_objetivo)
                print("Turno dado de baja con exito!")
                sleep(2)
            else:
                print("Error: el turno no existe!")
                sleep(2)
        if opcion_elegida == 7:  # Modificar turno
            dni_objetivo = ingresar_dni("Ingrese DNI del paciente asociado al turno: ")
            if existe_turno_asignado("Turnos", dni_objetivo):
                modificar_turno("Turnos", dni_objetivo, fechas_ocupadas_sin_dni)
                print("Turno modificado con exito!")
                sleep(2)
            else:
                print("Error: el turno no existe!")
                sleep(2)
        if opcion_elegida == 8:  # Mostrar turnos
            mostrar_turnos("Turnos")
            print("1) Búsqueda por DNI\n"
                  "2) Búsqueda por fecha\n"
                  "0) Volver")
            seleccion = ingresar_opcion("..: ", [1, 2, 0])
            if seleccion == 1:  # Búsqueda por DNI
                limpiar_consola()
                dni_objetivo = ingresar_dni("Ingrese DNI del paciente: ")
                if str(dni_objetivo) in dnis_activos:
                    print(obtener_turno("Turnos", dni_objetivo))
                else:
                    print("El paciente no se encuentra registrado!")
                print("0) Volver")
                seleccion = ingresar_opcion("..: ", [0])
            if seleccion == 2:  # Búsqueda por fecha
                limpiar_consola()
                lista_obtenida = buscador_turnos_dia("Turnos")
                ordenar_por_hora(lista_obtenida)
                mostrar_turnos_dia(lista_obtenida)
                print("0) Volver")
                seleccion = ingresar_opcion("..: ", [0])
                if seleccion == 0:
                    continue
            if seleccion == 0:
                continue
        if opcion_elegida == 9:  # Turnos del dia
            fecha_actual = datetime.date.today()
            fecha = [fecha_actual.day, fecha_actual.month, fecha_actual.year]
            ordenar_por_hora(fechas_ocupadas)
            cola_turnos = turnos_del_dia(fecha, fechas_ocupadas)
            salir = False
            while not salir:
                try:
                    limpiar_consola()
                    cola_turnos.imprimir_cola()
                    print()  # Salto de linea.
                    print("Turno actual: {}".format(cola_turnos.primero()))
                    print()  # Salto de linea.
                    print("1) Siguiente turno\n"
                          "0) Volver")
                    seleccion = ingresar_opcion("..: ", [1, 0])
                    if seleccion == 1:  # Siguiente turno
                        cola_turnos.desacolar()
                    if seleccion == 0:  # Volver
                        salir = True
                except ValueError:
                    print("No hay mas turnos!")
                    print()  # Salto de linea.
                    print("0) Volver")
                    seleccion = ingresar_opcion("..: ", [0])
                    if seleccion == 0:  # Volver
                        salir = True
                except:
                    print("Error inesperado!")
                    salir = True
                    sleep(2)
        if opcion_elegida == 0:  # Salir
            continuar = False
