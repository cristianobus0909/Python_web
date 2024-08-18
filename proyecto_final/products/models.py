from django.db import models
from accounts.models import UserProfile


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name
    
    


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, default='',blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    price = models.DecimalField(default=0, decimal_places=2,max_digits=6)
    image = models.ImageField(upload_to='upload/product/',default='upload/product/—Pngtree—a picture icon_4524748.png',blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    def __str__(self):
        return self.name

