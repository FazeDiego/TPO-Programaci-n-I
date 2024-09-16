from adicionales import *


def alta_paciente(fichero, dni):
    """
    Recibe un fichero como parametro y agrega al mismo los pacientes deseados con el siguiente formato:
    DNI;nombre y apellido;edad
    No produce salidas.
    """
    try:
        arch = open("{}.txt".format(fichero), "a")
        apellido = ingresar_apellido("Ingrese apellido: ")
        nombre = ingresar_nombre("Ingrese nombre: ")
        edad = ingresar_edad("Ingrese edad: ", [edad for edad in range(0, 18)])
        paciente = str(dni) + ";" + nombre + " " + apellido + ";" + str(edad) + '\n'
        arch.write(paciente)
        arch.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def baja_paciente(fichero, dni):
    """
    Recibe DNI del paciente y fichero de pacientes con formato DNI;nombre y apellido;edad como parametros.
    Elimina el paciente asociado.
    No produce salidas.
    """
    try:
        arch = open("{}.txt".format(fichero), "r")
        lineas_no_omitidas = []
        linea = arch.readline()
        linea_enlistada = linea.split(";")
        while linea != "":
            if not int(linea_enlistada[0]) == dni:
                lineas_no_omitidas.append(linea)
            linea = arch.readline()
            linea_enlistada = linea.split(";")
        arch.close()
        archivo = open("{}.txt".format(fichero), "w")
        archivo.writelines(lineas_no_omitidas)
        archivo.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def modificar_paciente(fichero, dni):
    """
    Recibe DNI del paciente y fichero de pacientes con formato DNI;nombre y apellido;edad como parametros.
    Solicita por teclado los datos actualizados y modifica al paciente con los mismos.
    No produce salidas.
    """
    try:
        archivo = open("{}.txt".format(fichero), "r")
        nuevo_apellido = ingresar_apellido("Ingrese el nuevo apellido: ")
        nuevo_nombre = ingresar_nombre("Ingrese el nuevo nombre: ")
        edad_actualizada = ingresar_edad("Ingrese la edad para actualizar: ", [edad for edad in range(0, 18)])
        lineas_no_omitidas = []
        linea = archivo.readline()
        linea_enlistada = linea.split(";")
        while linea != "":
            if int(linea_enlistada[0]) == dni:
                linea_enlistada[1] = nuevo_nombre + " " + nuevo_apellido
                linea_enlistada[2] = str(edad_actualizada) + "\n"
            lineas_no_omitidas.append(";".join(linea_enlistada))
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


def mostrar_pacientes(fichero):
    """
    Recibe un fichero de pacientes con formato DNI;nombre y apellido;edad como parametro e imprime los mismos en patanlla.
    No produce salidas.
    """
    try:
        arch = open("{}.txt".format(fichero), "r")
        for linea in arch:
            dni, nombre, edad = linea.split(";")
            print("DNI: {} Nombre: {} Edad: {}".format(dni, nombre, edad))
        arch.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def ordenar_por_nombre(fichero):
    """
    Recibe un fichero de pacientes con formato DNI;nombre y apellido;edad como parametro y ordena sus lineas
    alfabeticamente, segun los nombres de los pacientes.
    No produce salidas.
    """
    try:
        arch = open("{}.txt".format(fichero), "r")
        arch_lista = []
        for linea in arch:
            arch_lista.append(linea.split(";"))
        # ordenamiento_seleccion
        posiciones = len(arch_lista)
        for i in range(posiciones):
            for j in range(i + 1, posiciones):
                if arch_lista[i][1][:1] > arch_lista[j][1][:1]:
                    auxiliar = arch_lista[i]
                    arch_lista[i] = arch_lista[j]
                    arch_lista[j] = auxiliar
        arch.close()
        arch = open("{}.txt".format(fichero), "w")
        for linea in range(len(arch_lista)):
            arch.write(";".join(arch_lista[linea]))
        arch.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def ordenar_por_edad(fichero):
    """
    Recibe un fichero de pacientes con formato DNI;nombre y apellido;edad como parametro y ordena sus lineas segun la
    edad de los pacientes.
    No produce salidas.
    """
    try:
        arch = open("{}.txt".format(fichero), "r")
        arch_lista = []
        for linea in arch:
            arch_lista.append(linea.split(";"))
        # ordenamiento_seleccion
        posiciones = len(arch_lista)
        for i in range(posiciones):
            for j in range(i + 1, posiciones):
                if int(arch_lista[i][2]) > int(arch_lista[j][2]):
                    auxiliar = arch_lista[i]
                    arch_lista[i] = arch_lista[j]
                    arch_lista[j] = auxiliar
        arch.close()
        arch = open("{}.txt".format(fichero), "w")
        for linea in range(len(arch_lista)):
            arch.write(";".join(arch_lista[linea]))
        arch.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def filtrar_por_edad(filtro, fichero):
    """
    Recibe un fichero de pacientes con formato DNI;nombre y apellido;edad como parametro e imprime los que que sean
    mayor o igual a la edad deseada en patanlla.
    No produce salidas.
    """
    try:
        arch = open("{}.txt".format(fichero), "r")
        for linea in arch:
            dni, nombre, edad = linea.split(";")
            if int(edad) >= filtro:
                print("DNI: {} Nombre: {} Edad: {}".format(dni, nombre, edad))
        arch.close()
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def existe_paciente(fichero, dni):  # Sin uso
    """
    Recibe DNI del paciente y fichero de pacientes con formato DNI;nombre y apellido;edad como parametros.
    Retorna True si existe un paciente asociado o False en caso contrario.
    """
    try:
        archivo = open("{}.txt".format(fichero), "r")
        existencia = False
        linea = archivo.readline()
        linea_enlistada = linea.split(";")
        while linea != "":
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
