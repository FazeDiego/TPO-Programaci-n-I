from adicionales import *
from class_cola import *
import datetime


def alta_turno(fichero, dni, fechas_asignadas=[]):
    """
    Recibe DNI del paciente y fichero de turnos con formato DNI;dia;mes;año;hora como parametros y agrega al mismo un
    turno con el siguiente formato: DNI;dia;mes;año;hora. Adicionalmente recibe una lista con de fechas y horarios
    asignados hasta el momento para no repetir los mismos (opcional).
    No produce salidas.
    """
    while True:
        try:
            archivo = open("{}.txt".format(fichero), "a")
            dia = ingresar_dia("Ingrese el dia del turno: ", [1, 8, 15, 22])
            mes = ingresar_mes("Ingrese el mes: ")
            anio = ingresar_anio("Ingrese el año: ")
            hora = ingresar_hora("Ingrese la hora: ",
                                 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
            fecha_ingresada = datetime.date(anio, mes, dia)
            fecha_actual = datetime.date.today()
            assert fecha_ingresada >= fecha_actual, "Error: la fecha solicitada no se encuentra disponible, " \
                                                    "pruebe con la actual o posterior"
            turno = [str(dni), str(dia), str(mes), str(anio), str(hora)]
            fecha = [dia, mes, anio, hora]
            assert fecha not in fechas_asignadas, "Error: el horario en la fecha solicitada no se encuentra disponible"
            cadena_turno = ";".join(turno)
            archivo.write(cadena_turno + "\n")
            archivo.close()
            break
        except IOError:
            print("Error: no se pudo acceder al fichero")
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except:
            print("Error inesperado!")


def baja_turno(fichero, dni):
    """
    Recibe DNI del paciente y fichero de turnos con formato DNI;dia;mes;año;hora como parametros.
    Elimina el turno asociado.
    No produce salidas.
    """
    try:
        archivo = open("{}.txt".format(fichero), "r")
        lineas_no_omitidas = []
        linea = archivo.readline()
        linea_enlistada = linea.split(";")
        while linea != "":
            if not int(linea_enlistada[0]) == dni:
                lineas_no_omitidas.append(linea)
            linea = archivo.readline()
            linea_enlistada = linea.split(";")
        archivo.close()
        archivo = open("{}.txt".format(fichero), "w")
        archivo.writelines(lineas_no_omitidas)
        archivo.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def modificar_turno(fichero, dni, fechas_asignadas=[]):
    """
    Recibe DNI del paciente y fichero de turnos con formato DNI;dia;mes;año;hora como parametros.
    Solicita por teclado los datos actualizados y modifica el turno con los mismos.
    No produce salidas.
    """
    while True:
        try:
            archivo = open("{}.txt".format(fichero), "r")
            nuevo_dia = ingresar_dia("Ingrese el nuevo dia del turno: ", [1, 8, 15, 22])
            nuevo_mes = ingresar_mes("Ingrese el nuevo mes: ")
            nuevo_anio = ingresar_anio("Ingrese el nuevo año: ")
            nueva_hora = ingresar_hora("Ingrese la nueva hora: ",
                                       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
            lineas_no_omitidas = []
            linea = archivo.readline()
            linea_enlistada = linea.split(";")
            while linea != "":
                if int(linea_enlistada[0]) == dni:
                    linea_enlistada[1] = str(nuevo_dia)
                    linea_enlistada[2] = str(nuevo_mes)
                    linea_enlistada[3] = str(nuevo_anio)
                    linea_enlistada[4] = str(nueva_hora) + "\n"
                lineas_no_omitidas.append(";".join(linea_enlistada))
                linea = archivo.readline()
                linea_enlistada = linea.split(";")
            archivo.close()
            fecha_ingresada = datetime.date(nuevo_anio, nuevo_mes, nuevo_dia)
            fecha_actual = datetime.date.today()
            assert fecha_ingresada >= fecha_actual, "Error: la fecha solicitada no se encuentra disponible, " \
                                                    "pruebe con la actual o posterior"
            fecha = [nuevo_dia, nuevo_mes, nuevo_anio, nueva_hora]
            assert fecha not in fechas_asignadas, "Error: el horario en la fecha solicitada no se encuentra disponible"
            archivo = open("{}.txt".format(fichero), "w")
            archivo.writelines(lineas_no_omitidas)
            archivo.close()
            break
        except IOError:
            print("Error: no se pudo acceder al fichero")
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except:
            print("Error inesperado!")


def mostrar_turnos(fichero):
    """
    Recibe un fichero de turnos con formato DNI;dia;mes;año;hora como parametro e imprime los mismos en patanlla.
    No produce salidas.
    """
    try:
        arch = open("{}.txt".format(fichero), "r")
        for linea in arch:
            dni, dia, mes, anio, hora = linea.split(";")
            print("DNI: {} Dia: {} Mes: {} Año: {} Hora: {}".format(dni, dia, mes, anio, hora))
        arch.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def existe_turno_asignado(fichero, dni):
    """
    Recibe DNI del paciente y fichero de turnos con formato DNI;dia;mes;año;hora como parametros.
    Retorna True si existe un turno asociado o False en caso contrario.
    """
    try:
        existencia = False
        archivo = open("{}.txt".format(fichero), "r")
        linea = archivo.readline()
        linea_enlistada = linea.split(";")
        while linea != "" and existencia == False:
            if int(linea_enlistada[0]) == dni:
                existencia = True
            linea = archivo.readline()
            linea_enlistada = linea.split(";")
        archivo.close()
        return existencia
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def obtener_turno(fichero, dni):
    """
    Recibe DNI del paciente y fichero de turnos con formato DNI;dia;mes;año;hora como parametros.
    Retorna la linea del fichero correspondiente al turno del DNI, o None en caso contrario.
    """
    try:
        turno = "Turno inexistente!"
        archivo = open("{}.txt".format(fichero), "r")
        linea = archivo.readline()
        linea_enlistada = linea.split(";")
        while linea != "" and turno == "Turno inexistente!":
            if int(linea_enlistada[0]) == dni:
                turno = "DNI: {} Dia: {} Mes: {} Año: {} Hora: {}".format(linea_enlistada[0], linea_enlistada[1],
                                                                          linea_enlistada[2], linea_enlistada[3],
                                                                          linea_enlistada[4])
            linea = archivo.readline()
            linea_enlistada = linea.split(";")
        archivo.close()
        return turno
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def ordenar_por_hora(lista):
    """
    Recibe un fichero de pacientes con formato DNI;nombre y apellido;edad como parametro y ordena sus lineas segun la
    hora.
    No produce salidas.
    """
    # ordenamiento_seleccion
    posiciones = len(lista)
    for i in range(posiciones):
        for j in range(i + 1, posiciones):
            if int(lista[i][4]) > int(lista[j][4]):
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar


def turnos_del_dia(fecha, lista_turnos):
    turnos_de_hoy = cola()
    turnos_de_hoy.incializar_cola()
    for i in range(len(lista_turnos)):
        if lista_turnos[i][1:4] == fecha:
            turno = "DNI: {} Dia: {} Mes: {} Año: {} Hora: {}".format(lista_turnos[i][0], lista_turnos[i][1],
                                                                      lista_turnos[i][2], lista_turnos[i][3],
                                                                      lista_turnos[i][4])
            turnos_de_hoy.acolar(turno)
    return turnos_de_hoy


def buscador_turnos_dia(fichero):
    validacion = True
    lista = enlistar_listas("Turnos", 0, 4)
    lista_diaria = []
    dia = ingresar_dia("Ingrese el dia de los turnos a enlistar: ", [1, 8, 15, 22])
    mes = ingresar_mes("Ingrese el mes: ")
    anio = ingresar_anio("Ingrese el año: ")
    while validacion == True:
        for i in range(len(lista)):
            particulares = []
            particulares.append(lista[i][0])
            if lista[i][1] == dia:
                particulares.append(dia)
            else:
                validacion = False
            if lista[i][2] == mes:
                particulares.append(mes)
            else:
                validacion = False
            if lista[i][3] == anio:
                particulares.append(anio)
                particulares.append(lista[i][4])
            else:
                validacion = False

            if len(particulares) == 5:
                lista_diaria.append(particulares)
            else:
                continue
        if validacion == False:
            if len(lista_diaria) <= 0:
                print("No se encontraron turnos en el dia solicitado")
            else:
                return lista_diaria


def mostrar_turnos_dia(lista):
    fil = len(lista)
    col = (len(lista[0]))
    diccionario = {'datos': ['DNI: ', '  Dia: ', '  Mes: ', '  Año: ', '  Hora: ']}
    for i in range(fil):
        print()
        for c in range(col):
            print(diccionario['datos'][c], end=' ')
            print(lista[i][c], end='')
    print()
