from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name='Inicio'),
    path('cursos/',cursos, name='Cursos'),
    path('profesores/',profesores,name='Profesores'),
    path('estudiantes/',estudiantes, name='Estudiantes'),
    path('curso-formulario/',cursos_formulario, name='CursoFormulario'),
    path('profesor-formulario/',profesor_formulario,name='ProfesorFormulario'),
    path('estudiante-formulario/',estudiante_formulario,name='EstudianteFormulario'),
    path('busquedaCamada/',busquedaCamada,name='BusquedaCamada'),
    path('buscar/',buscar,name='Buscar'),
]
