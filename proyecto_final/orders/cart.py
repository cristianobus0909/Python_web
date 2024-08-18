from products.models import Product
class Cart():
    def __init__(self,req):
        self.session = req.session
        cart = self.session.get('session_key')
        if 'session_key' not in req.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price': str(product.price)}
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    def get_products(self):
        products_id = self.cart.keys()
        products = Product.objects.filter(id_in= products_id)
        return products
