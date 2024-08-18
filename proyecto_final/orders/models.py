
from django.db import models
from accounts.models import UserProfile
from products.models import Product
import datetime

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=30,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Order {self.id} by {self.customer}"