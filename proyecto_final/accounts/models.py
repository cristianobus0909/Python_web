from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=255, default='Default Address')

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='avatares/Login_default_Avatar.png',upload_to='avatares', blank=True, null=True)
