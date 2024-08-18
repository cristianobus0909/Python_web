bd = {}
def registro (bd):
    nombre =  input("Ingrese su nombre: ")
    contraseña = input("Ingrese una contraseña segura: ")
    edad = input("ingrese su edad")
    email = input("Ingrese su email")
    nuevo_usuario = {
        'nombre': nombre,
        'contraseña': contraseña,
        'edad': edad,
        'email': email
    }
    if len(bd) == 0:
        bd.update(nuevo_usuario)
    else:
        print("Ya existe un usuario registrado.")
    return bd

def leer_data(bd):
    for key, value in bd.items():
        print(f"{key}: {value}")

def login(bd):
    nombre = input ("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese  su contraseña: ")
    while nombre  != bd.get('nombre') or contraseña != bd.get('contraseña'):
        print("Usuario o Contraseña incorrecta")
        nombre = input ("Intente nuevamente ingresando su nombre de usuario: ")
        contraseña = input("Intente nuevamente ingresando su contraseña: ")
    else:
        print("Bienvenido", nombre)
    return bd

registro(bd)
leer_data(bd)
login(bd)
