from package_1.user import User
from package_1.products import *



name =  input("Ingrese su nombre: ")
last_name = input("Ingrese su Apellido: ")
age = input("ingrese su edad: ")
email = input("Ingrese su email: ")
password = input("Ingrese su contraseña: ")
credit = input("Ingrese el monto de su presupuesto que dispone para comprar: ")

new_user1 = User(name,last_name,age,email,password)
print(new_user1)

email_for_login = input("Ingrese su email para ingresar: ")
password_for_login = input("Ingrese su contraseña para ingresar: ")
logged = new_user1.login(email_for_login, password_for_login)

while logged:
    print("Bienvenido a la tienda de celulares")
    option_selected = input(
        """¿Que desea hacer? Ingrese un numero:
        1. Ver los productos
        2. Comprar un producto
        3. Cambiar contraseña
        4. Salir
        """
    ) 
    if option_selected == "1":
        read_db_products()
    elif option_selected == "2":
        try:
            id_product = int(input("Introduce el ID del producto que deseas agregar al carrito: "))
            product = get_product(id_product)
            if product:
                cart = add_to_cart(product)
                sale = input("Para comprar ingresa: 'S'")
                if sale.lower() == "s":
                    buy_cart(cart, credit)
            else:
                print("Producto no encontrado.")
        except ValueError:
            print("Error: Introduce un número válido para el ID.")
    elif option_selected == "3":
        password_confirm = input("Ingrese su contraseña: ")
        update_user = new_user1.update(password_confirm)
    elif option_selected == "4":
        print("Gracias por su visita")
        break
else: 
    print("El usuario no existe")