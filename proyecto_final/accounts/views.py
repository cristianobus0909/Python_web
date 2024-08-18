from django.shortcuts import render, redirect
from .forms import UserEditForm, AvatarForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Avatar


# Create your views here.
def index(req):
    avatar_url = None
    if req.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=req.user)
            avatar_url = avatar.imagen.url
        except Avatar.DoesNotExist:
            avatar_url = None

    return render(req, 'index.html', {"url": avatar_url})

@csrf_protect
def login_view(req):
    if req.method == 'POST':
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password')
            
            user = authenticate(username=user_name, password=user_password)

            if user is not None:
                login(req, user)
                req.session['username'] = user_name
                return render(req,'profile.html',{'user': user})
            else:
                return render(req, 'login.html', {'form': form, "message": "Credenciales incorrectas"})
        else:
            return render(req, 'login.html', {'form': form, "message": "Formulario inválido"})    
    else:
        form = AuthenticationForm()
    return render(req,'login.html',{'form':form})

def signup_view(req):
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect('login')
        else:
            return render(req, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(req, 'signup.html', {'form': form})

@login_required
def profile_view(req):
    user = req.user
    
    try:
        avatar = Avatar.objects.get(user=user)
        avatar_url = avatar.imagen.url
    except Avatar.DoesNotExist:
        avatar_url = None
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'age': getattr(user, 'age', 'No especificado'),  
        'address': getattr(user, 'address', 'No especificado'),
        'avatar_url': avatar_url,
    }
    return render(req, 'profile.html', context)

@login_required
def profile_edit(req):
    user = req.user
    try:
        avatar = Avatar.objects.get(user=user)
    except Avatar.DoesNotExist:
        avatar = Avatar(user=user)

    if req.method == 'POST':
        form = UserEditForm(req.POST, instance= user)
        avatar_form = AvatarForm(req.POST, req.FILES, instance=avatar)
        if form.is_valid() and avatar_form.is_valid():
            data = form.cleaned_data
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.age = data['age']
            user.address = data['address']
            if data['password1']:
                user.set_password(data['password1'])
            
            user.save()
            avatar.save()
            
            return render(req,'profile.html', {'avatar_url': avatar.imagen.url})
        else:
            return render(req, 'profileEditForm.html', {'form': form, 'avatar_form': avatar_form})
    else:
        form = UserEditForm(instance= user)
        avatar_form = AvatarForm(instance=avatar)
        return render(req, 'profileEditForm.html', {'form': form, 'avatar_form': avatar_form})
def about(req):
    return render(req, 'about.html', {})