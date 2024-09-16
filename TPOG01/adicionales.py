def titulo():
    """
    Imprime por pantalla el titulo principal del programa.
    """
    texto = "   ██╗░░░██╗░█████╗░██████╗░███████╗  ███╗░░░███╗███████╗██████╗░██╗░█████╗░░█████╗░██╗░░░░░\n" \
            "   ██║░░░██║██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░\n" \
            "   ██║░░░██║███████║██║░░██║█████╗░░  ██╔████╔██║█████╗░░██║░░██║██║██║░░╚═╝███████║██║░░░░░\n" \
            "   ██║░░░██║██╔══██║██║░░██║██╔══╝░░  ██║╚██╔╝██║██╔══╝░░██║░░██║██║██║░░██╗██╔══██║██║░░░░░\n" \
            "   ╚██████╔╝██║░░██║██████╔╝███████╗  ██║░╚═╝░██║███████╗██████╔╝██║╚█████╔╝██║░░██║███████╗\n" \
            "   ░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝  ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝\n"

    print()  # Salto de linea.
    print(texto)
    print()  # Salto de linea.


def info():
    texto = "Profesor:  Escalante Leiva Ezequiel Ramiro\n" \
            "Alumnos:   Castellanos Ivan\n" \
            "           Banchio Ezequiel\n" \
            "           Martinez Auqui Diego Joaquin\n" \
            "           Bozzer San Miguel Juan Bautista\n" \
            "           Anderson Francisco\n" \
            "           Navarte Gonzalo\n"
    print()  # Salto de linea.
    print(texto)
    print()  # Salto de linea.


def ingresar_dni(msj, inicial=1000000, final=99999999):
    """
    Recibe una cadena de texto para solicitar el DNI y dos valores incial-final para limitar el ingreso del mismo en
    el rango deseado, como parametros.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna DNI (numero entero)
    """
    while True:
        try:
            dni = int(input(msj))
            assert inicial <= dni <= final, "Error: DNI fuera de rango!"
            assert type(dni) == int, "Error: ingreso un numero de punto flotante, este debe ser entero."
            return dni
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_nombre(msj):
    """
    Recibe una cadena de texto para solicitar un nombre no alfanumerico como parametro.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna nombre (cadena de texto)
    """
    while True:
        try:
            nombre = input(msj)
            nombres = nombre.split(" ")
            for n in range(len(nombres)):
                assert nombres[n].isalpha() == True, "Error: ingreso un numero o caracter invalido."
            return nombre.title()
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_apellido(msj):
    """
    Recibe una cadena de texto para solicitar un apellido no alfanumerico como parametro.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna apellido (cadena de texto)
    """
    while True:
        try:
            apellido = input(msj)
            apellidos = apellido.split(" ")
            for a in range(len(apellidos)):
                assert apellidos[a].isalpha() == True, "Error: ingreso un numero o caracter invalido."
            return apellido
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_edad(msj, exceptuar=[-1], inicial=0, final=120):
    """
    Recibe una cadena de texto para solicitar una edad, una lista de valores a exceptuar y dos valores incial-final
    para limitar el ingreso de la misma en el rango deseado, como parametros.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna edad (numero entero)
    """
    while True:
        try:
            edad = float(input(msj))
            assert inicial <= edad <= final, "Error: edad fuera de rango!"
            assert not edad in exceptuar, "Error: edad no habilitada!"
            assert edad == int(edad), "Error: ingreso un numero de punto flotante, este debe ser entero."
            return int(edad)
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_dia(msj, exceptuar=[0], inicial=1, final=31):
    """
    Recibe una cadena de texto para solicitar un dia, una lista de valores a exceptuar y dos valores incial-final
    para limitar el ingreso de la misma en el rango deseado, como parametros.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna dia (numero entero)
    """
    while True:
        try:
            dia = float(input(msj))
            assert inicial <= dia <= final, "Error: dia fuera de rango!"
            assert not dia in exceptuar, "Error: dia no habilitado!"
            assert dia == int(dia), "Error: ingreso un numero de punto flotante, este debe ser entero."
            return int(dia)
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_mes(msj, exceptuar=[0], inicial=1, final=12):
    """
    Recibe una cadena de texto para solicitar un mes, una lista de valores a exceptuar y dos valores incial-final
    para limitar el ingreso de la misma en el rango deseado, como parametros.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna mes (numero entero)
    """
    while True:
        try:
            mes = float(input(msj))
            assert inicial <= mes <= final, "Error: mes fuera de rango!"
            assert not mes in exceptuar, "Error: mes no habilitado!"
            assert mes == int(mes), "Error: ingreso un numero de punto flotante, este debe ser entero."
            return int(mes)
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_anio(msj, exceptuar=[-1], inicial=1900, final=3000):
    """
    Recibe una cadena de texto para solicitar un año, una lista de valores a exceptuar y dos valores incial-final
    para limitar el ingreso de la misma en el rango deseado, como parametros.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna año (numero entero)
    """
    while True:
        try:
            anio = float(input(msj))
            assert inicial <= anio <= final, "Error: año fuera de rango!"
            assert not anio in exceptuar, "Error: año no habilitado!"
            assert anio == int(anio), "Error: ingreso un numero de punto flotante, este debe ser entero."
            return int(anio)
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_hora(msj, exceptuar=[0], inicial=0, final=24):
    """
    Recibe una cadena de texto para solicitar una hora, una lista de valores a exceptuar y dos valores incial-final
    para limitar el ingreso de la misma en el rango deseado, como parametros.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna hora (numero entero)
    """
    while True:
        try:
            hora = float(input(msj))
            assert inicial <= hora <= final, "Error: hora fuera de rango!"
            assert not hora in exceptuar, "Error: hora no habilitada!"
            assert hora == int(hora), "Error: ingreso un numero de punto flotante, este debe ser entero."
            return int(hora)
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def ingresar_opcion(msj, opciones=[0]):
    """
    Recibe una cadena de texto para solicitar una opción y una lista con los valores disponibles para la misma.
    Solicita por teclado con el mensaje previamente cargado y valida su ingreso.
    Retorna opción (numero entero)
    """
    while True:
        try:
            opcion = int(input(msj))
            assert opcion in opciones, "Error: opcion {} inexistente!".format(opcion)
            return opcion
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except ValueError:
            print("Error: ingreso invalido!")
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
            print()  # Salto de linea.


def enlistar_columna_fichero(fichero, campo):
    """
    Recibe fichero y valor correspondiente a un campo valido como parametros.
    Enlista la columna de esta campo y la retorna.
    """
    try:
        archivo = open("{}.txt".format(fichero), "r")
        columna_enlistada = []
        linea = archivo.readline()
        linea_enlistada = linea.split(";")
        while linea != "":
            columna_enlistada.append(linea_enlistada[campo])
            linea = archivo.readline()
            linea_enlistada = linea.split(";")
        archivo.close()
        return columna_enlistada
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")


def eliminar_valor(lista, valor):
    """
    Recibe lista y valor a eliminar.
    """
    try:
        pos = lista.index(valor)
        lista.pop(pos)
    except ValueError:
        print("Error: el valor no se encuentra.")
    except:
        print("Error inesperado!")


def enlistar_listas(fichero, desde, hasta):
    """
    Recibe fichero y rango correspondiente a campos numericos, validos y consecutivos como parametros.
    Enlista los campos en el rango deseado de cada fila y retorna una lista de listas.
    """
    try:
        archivo = open("{}.txt".format(fichero), "r")
        listas_enlistadas = []
        linea = archivo.readline()
        linea_enlistada = linea.split(";")
        while linea != "":
            lista = [int(linea_enlistada[i]) for i in range(desde, hasta + 1)]
            listas_enlistadas.append(lista)
            linea = archivo.readline()
            linea_enlistada = linea.split(";")
        archivo.close()
        return listas_enlistadas
    except IOError:
        print("Error: no se pudo acceder al fichero")
    except:
        print("Error inesperado!")
