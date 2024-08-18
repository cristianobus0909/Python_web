from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup/',signup_view, name='signup'),
    path('about/',about, name='about'),
    path('login/',login_view, name='login'),
    path('profile/',profile_view, name='profile'),
    path('profile/edit/',profile_edit, name='profile_edit'),
    path('logout/',LogoutView.as_view(template_name='logout.html'), name='logout')
]