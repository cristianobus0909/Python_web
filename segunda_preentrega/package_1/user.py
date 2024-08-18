

class User():
    def __init__(self, name, last_name, age, email,password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
    def __str__(self):
        return f"Ususario: {self.name} registrado"
    def login(self,email, password):
        if self.email == email and self.password == password:
            return True
        else:
            'Usuario y contraseña incorrectos'
            return False
    def update(self, password):
        if password != self.password:
            self.password = password
            print('Contraseña actualizada con exito')
        else:
            print('Vuelva a intentarlo. Gracias')




