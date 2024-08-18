from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Ingrese su email:', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label='Edad', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Domicilio', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control password-input'}))
    password2 = forms.CharField(label='Repetir Contraseña', required=False, widget=forms.PasswordInput(attrs={'class': 'form-control password-input'}))
    
    class Meta:
        model = UserProfile
        fields = ['email', 'last_name', 'first_name', 'age', 'address']

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Deben cohincidir las contraseñas')
        return password2

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }