# Programa para registro y almacenamiento de usuarios

# Diccionario de usuarios y contraseñas (base de datos)
usuarios = {}

def agregar_usuario():
    """
    Función para registrar usuario y contraseña en el diccionario.
    """
    usuario = input("Ingrese el nombre de usuario: ")
    contrasena = input("Ingrese la contraseña: ")
    usuarios[usuario] = contrasena
    print(f"Usuario {usuario} agregado correctamente.")

def mostrar_usuarios():
    """
    Función para leer los datos registrados.
    """
    print("\nLa info almacenada en la base de datos es:")
    for usuario, contrasena in usuarios.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")

def guardar_en_archivo():
    """
    Función para guardar los datos registrados, en un archivo txt EN LA CARPETA RAÍZ DEL PROGRAMA.
    """
    with open("usuarios.txt", "w") as archivo:
        for usuario, contrasena in usuarios.items():
            archivo.write(f"{usuario}:{contrasena}\n")
    print("Datos guardados en usuarios.txt")

def login():
    """
    Función para verificar el inicio de sesión.
    """
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    if usuario in usuarios and usuarios[usuario] == contrasena:
        print("Has iniciado sesión!")
    else:
        print("Usuario o contraseña incorrectos")

def main():
    """
    MENÚ.
    """
    while True:
        print("\nMenú:")
        print("1. Registrar usuario")
        print("2. Leer registros")
        print("3. Guardar registros en txt")
        print("4. Iniciar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            guardar_en_archivo()
        elif opcion == "4":
            login()
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()