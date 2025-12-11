import time
libros = {}
usuarios = {}
prestamos = []
# titulo


def registrar_libro(titulo, autor, cantidad):
    if titulo in libros:
        print(f"el libro {titulo} ya esta reguistrado")
    else:
        libros[titulo] = {
            "autor": autor,
            "cantidad": cantidad
        }
        print(f"le libro {titulo} fue reguistrado exitosamente ")

# nombre
# dni


def registrar_usuario(nombre, dni):
    if dni in usuarios:
        print(f"el usuario {dni} ya esta registrado")
    else:
        usuarios[dni] = {
            "nombre": nombre,
            "dni": dni
        }


def prestar_libro(titulo, dni_usuario):
    if titulo not in libros:
        print(f"el libro {titulo} no esta registrado")
        return
    if dni_usuario not in usuarios:
        print(f" el usuario con el dni {dni_usuario} no esta reguistrado ")
        return
    if libros[titulo]["cantidad"] <= 0:
        print("no hay copias de este libro")

    prestamos.append({
        "libro": titulo,
        "dni": dni_usuario,
        "nombre": usuarios[dni_usuario]["nombre"]
    })
    libros[titulo]["cantidad"] -= 1
    print(f"el libro {titulo} fu prestado a {usuarios[dni_usuario]['nombre']}")


def devolver_libro(titulo, dni_usuario):
    encotrado = None
    for prestamo in prestamos:
        if prestamo['libro'] == titulo and prestamo["dni"] == dni_usuario:
            encotrado = prestamo
        break
    if not encotrado:
        print(f"el libro {titulo} no fue pretado en esta instalacion")

    libros[titulo]["cantidad"] += 1
    print(
        f"el libto {titulo} que fue pretado a {usuarios[dni_usuario]['nombre']}")


def ver_libros_disponibles():
    for titulo, info in libros.items():
        print(
            f"los libros disponibles son {titulo}: y la cantidad es {info['cantidad']}")


def ver_prestamos_activos():
    if not prestamos:
        print("no hay prestamos activos ")
        return
    for prestamo in prestamos:
        titulo = prestamo["libro"]
        dni = prestamo["dni"]
        nombre = usuarios[dni]["nombre"]
        print(f"los titulos pretados son {prestamo} a {nombre}(DNI {dni})")


while True:
    print("** MENU PRINCIPAL**")
    print("\n escoges unas e las siguientes opciones ")
    print("1️  Registrar libro")
    print("2️  Registrar usuario")
    print("3️  Prestar libro")
    print("4️  Devolver libro")
    print("5️  Ver préstamos activos")
    print("6️  Ver libros disponibles")
    print("0️  Salir")

    opcion = int(input("cual es tu opccion: "))

    if opcion == 0:
        print("saliendo gracias ")

        break
    

    elif opcion == 1:
        titulo = input("ingresa el titulo de tu libro: ")
        autor = input("ingresa el nombre de el escritos de el libro: ")
        cantidad = int(input("ingresa  la cantidad de libros que vas a ingresar: "))
        registrar_libro(titulo, autor, cantidad)
        print(f"DEBUG - Libros guardados: {libros}")
        time.sleep(3)

    elif opcion == 2:
        nombre = input("cual es tu nombre: ")
        dni = int(input("ingresa ti ti DNI: "))
        registrar_usuario(nombre, dni)
        print(f"DEBUG - Libros guardados: {usuarios}")
        time.sleep(3)

    elif opcion == 3:
        titulo = input("nombre de el libro que deseas: ")
        dni_usuario = int(input("ingresa ti ti DNI: "))
        prestar_libro(titulo, dni_usuario)
        time.sleep(3)

    elif opcion == 4:
        titulo = input("nombre de el libro que deseas devolver: ")
        dni_usuario = int(input("ingresa ti ti DNI: "))
        devolver_libro(titulo, dni_usuario)
        time.sleep(3)

    elif opcion == 5:
        ver_libros_disponibles()
        print(f"los libros activos son {libros}")
        time.sleep(3)

    elif opcion == 6:
        
        ver_prestamos_activos()
        time.sleep(3)

