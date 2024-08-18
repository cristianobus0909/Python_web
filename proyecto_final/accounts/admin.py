from django.contrib import admin
from .models import UserProfile, Avatar

# Register your models here.
@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'last_name', 'email', 'age', 'address')

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'imagen')