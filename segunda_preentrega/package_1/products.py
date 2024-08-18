lista_de_precios = [
    {"id":1,"product": "celular", "price": 1000},
    {"id":2,"product": "funda", "price": 200},
    {"id":3,"product": "cargador", "price": 300},
    {"id":4,"product": "memoria", "price": 400}
]

cart = []
def read_db_products():
    for producto in lista_de_precios:
        print(f'ID: {producto["id"]}, Producto: {producto["product"]}, Precio: ${producto["price"]}')
def get_product(id):
    for producto in lista_de_precios:
        if producto["id"] == id:
            return producto
    return None

def add_to_cart(product):
    cart.append(product)
    print(f'Producto {product["product"]} agregado al carrito.')
    return cart
def buy_cart(cart, credit):
    print(cart, credit)
    total_spent = 0
    credit = int(credit)
    while credit != 0:
        made_purchase = False
        for product in cart:
            if credit >= product["price"]:
                credit -= product["price"]
                total_spent += product["price"]
                print(f'Producto comprado: {product["product"]} por {product["price"]}')
                made_purchase = True
                cart.remove(product)
                break
            else:
                print(f'No tienes suficiente dinero para comprar {product["name"]} por {product["price"]}')
        if not made_purchase:
            break
    if credit == 0:
        print("Has gastado todo tu crédito.")
    else:
        print(f'Te queda un crédito de {credit}')