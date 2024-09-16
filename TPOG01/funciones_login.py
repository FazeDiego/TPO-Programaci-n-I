def registro(fichero):
    """
    Recibe un fichero como parametro y agrega al mismo las credenciales deseadas con el siguiente formato:
    usuario;contraseña
    No produce salidas.
    """
    archivo = open("{}.txt".format(fichero), "a") #a de append
    while True:
        try:
            usuario = input("Ingrese el usario deseado: ")
            assert not usuario == "", "Error: no ingreso usuario."
            while True:
                try:
                    contrasenia = input("Ingrese contraseña: ")
                    assert not contrasenia == "", "Error: no ingreso contraseña."
                    confirmada = input("Confirme contraseña: ")
                    assert (contrasenia == confirmada), "Error: las contraseñas no coinciden."
                    break
                except AssertionError as err:
                    print(err)
                    print()  # Salto de linea.
            break
        except AssertionError as err:
            print(err)
            print()  # Salto de linea.
        except:
            print("Error inesperado!")
    credenciales = [usuario, contrasenia]
    cadena = ";".join(credenciales)
    archivo.write(cadena + "\n")
    archivo.close()


def inicio_sesion(fichero):
    """
    Recibe un fichero de credenciales con formato usuario;contraseña como parametro.
    Solicita por teclado usuario y contraseña, y verifica su existencia como pareja dentro del fichero.
    Retorna True si este par existe o False en caso contrario.
    """
    while True:
        try:
            estado = False
            archivo = open("{}.txt".format(fichero), "r")
            while True:
                try:
                    usuario = input("Ingrese usario: ")
                    assert not usuario == "", "Error: no ingreso usuario."
                    while True:
                        try:
                            contrasenia = input("Ingrese contraseña: ")
                            assert not contrasenia == "", "Error: no ingreso contraseña."
                            break
                        except AssertionError as err:
                            print(err)
                            print()  # Salto de linea.
                    break
                except AssertionError as err:
                    print(err)
                    print()  # Salto de linea.
                except:
                    print("Error inesperado!")
            credenciales = [usuario, contrasenia]
            cadena = ";".join(credenciales)
            for linea in archivo:
                if cadena + "\n" == linea:  # "usuario;contraseña\n (ingresada) == "usuario;contraseña\n (registrada)
                    estado = True
            return estado
        except FileNotFoundError:
            archivo = open("{}.txt".format(fichero), "w")
            archivo.close()
