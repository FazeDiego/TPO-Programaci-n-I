from funciones_login import *
from menu_principal import *
from generador import cargar_datos_prueba

limpiar_consola = lambda: system("cls")


def main():
    while True:
        limpiar_consola()
        titulo()
        print("1) Iniciar sesión\n"
              "2) Registrarse\n"
              "3) Cargar datos de prueba\n"
              "4) Info\n"
              "0) Salir")
        opcion_elegida = ingresar_opcion("..: ", [1, 2, 3, 4, 0])
        print()  # Salto de linea.

        if opcion_elegida == 1:
            intentos_fallidos = 1
            limpiar_consola()
            titulo()
            acceso = inicio_sesion("Usuarios")
            while acceso == False and not intentos_fallidos == 3:
                intentos_fallidos = intentos_fallidos + 1
                limpiar_consola()
                titulo()
                if intentos_fallidos >= 1:
                    print("Error de acceso: Nombre de usuario o contraseña incorrecta. "
                          "Intento: {}".format(intentos_fallidos))
                    print("Intente nuevamente...")
                    print()  # Salto de linea.
                acceso = inicio_sesion("Usuarios")
            if acceso:
                limpiar_consola()
                titulo()
                menu()
            else:
                limpiar_consola()
                titulo()
                print("Intentos fallidos: 3\n"
                      "Acceso denegado")
                sleep(3)
        if opcion_elegida == 2:
            limpiar_consola()
            titulo()
            registro("Usuarios")
        if opcion_elegida == 3:
            cargar_datos_prueba()
            print("Datos de prueba cargados correctamente!")
            sleep(2)
        if opcion_elegida == 4:
            limpiar_consola()
            titulo()
            info()
            print("0) Volver")
            seleccion = ingresar_opcion("..: ", [0])
            if seleccion == 0:
                continue
        if opcion_elegida == 0:
            limpiar_consola()
            titulo()
            print("Finalizando...")
            sleep(2)
            break


main()
