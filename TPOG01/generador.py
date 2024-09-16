from datetime import datetime


def cargar_datos_prueba():
    """
    Genera tres ficheros para probar el correcto funciomiento del programa principal. Usuarios.txt, Pacientes.txt,
    Turnos.txt
    """
    fecha_actual = datetime.now()
    usuarios = open("Usuarios.txt", "w")
    pacientes = open("Pacientes.txt", "w")
    turnos = open("Turnos.txt", "w")

    lista_usuarios = ["admin;admin\n", "user;user\n"]
    lista_pacientes = ["34003400;Lionel Messi;34\n", "36003600;Cristiano Ronaldo;36\n", "35003500;Sergio Ramos;35\n",
                       "34340000;Luis Suarez;34\n", "28002800;Paul Pogba;28\n", "38003800;Dani Alves;38\n"]
    lista_turnos = ["34003400;{};{};{};10\n".format(fecha_actual.day, fecha_actual.month, fecha_actual.year),
                    "36003600;{};{};{};11\n".format(fecha_actual.day, fecha_actual.month, fecha_actual.year),
                    "35003500;{};{};{};12\n".format(fecha_actual.day, fecha_actual.month, fecha_actual.year),
                    "34340000;{};{};{};13\n".format(fecha_actual.day + 1, fecha_actual.month, fecha_actual.year),
                    "28002800;{};{};{};14\n".format(fecha_actual.day + 1, fecha_actual.month, fecha_actual.year),
                    "38003800;{};{};{};10\n".format(fecha_actual.day + 2, fecha_actual.month, fecha_actual.year)]
    usuarios.writelines(lista_usuarios)
    pacientes.writelines(lista_pacientes)
    turnos.writelines(lista_turnos)

    usuarios.close()
    pacientes.close()
    turnos.close()
