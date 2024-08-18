# Django Project README

## Descripción del Proyecto

Este proyecto es una aplicación web creada con Django. El proyecto incluye funcionalidades básicas como la creación de formularios, manejo de URLs y vistas para procesar y mostrar datos.

## Requisitos

- Python 3.x
- Django 3.x o superior

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/cristianobus0909/python_web.git
    cd tercera_preentrega
    ```

2. Crea y activa un entorno virtual:
    ```sh
    pipenv shell
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install django
    ```

4. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Creación de URLs

En Django, las URLs se definen en el archivo `urls.py` de cada aplicación y en el archivo `urls.py` del proyecto principal.

1. **Definir URLs en la aplicación**:
    Crea un archivo `urls.py` en la carpeta de tu aplicación (si no existe) y agregar las rutas necesarias para renderizar las vistas de cursos, estudiantes, profesores, formularios para registrar nuevos cursos, estudiantes y profesores

    ```python
    # app/urls.py
    from django.urls import path
    from . import views

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
    ```

2. **Incluir URLs de la aplicación en el proyecto**:
    Modifica el archivo `urls.py` del proyecto principal para incluir las URLs de la aplicación.

    ```python
    # project/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('app.urls')),
    ]
    ```

## Creación de Vistas

Las vistas en Django son funciones que manejan las solicitudes HTTP y devuelven respuestas. Aquí se muestran ejemplos de vistas simples para manejar el inicio y un formulario de cursos.

```python
# app/views.py
from django.shortcuts import render
from .forms import CursoFormulario

def inicio(request):
    return render(request, 'index.html')

def cursos_formulario(request):
    if request.method == 'POST':
        form = CursoFormulario(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, 'index.html', {'mensaje': 'Curso creado exitosamente'})
    else:
        form = CursoFormulario()
    return render(request, 'curso_formulario.html', {'form': form})
```
## Prueba de rutas y vistas

Ya creadas las vistas con sus respectivas funcionalidades que nos renderizan diferentes endpoints, ahora, realizamos las respectivas pruevas para comprobar que todo funciona correctamente

1. **Levantamos el proyecto en el navegador**:
    Una vez iniciado(Sigue el paso 5. en apartado de Instalacion), Django nos provee una url de nuestro proyecto `http://127.0.0.1:8000/` o podemos indicar con que puerto queremos iniciar escribiendo `python manage.py runserver 3000` por ejemplo
2. **Desde el Navbar**:
    Apretando en Inicio nos lleva a un mensaje que indica que estamos en inicio. De igual forma en las demas opciones(Cursos, Estudiantes, Profesores) apretando nos muestra informacion obtenida de la base de datos y si no encuentra nos muestra un mensaje 
3. **Desde barra de direcciones**:
    Al ingresar, siguiendo el ejemplo: `http://127.0.0.1:8000/admin`, ingresamos al panel de administrador donde podemos agregar nuevos registros a las listas.
    Al ingresar, siguiendo el ejemplo: `http://127.0.0.1:8000/app-coder/curso-formulario/`, nos devuelve un formulario para crear un nuevo curso.
    Al ingresar, siguiendo el ejemplo: `http://127.0.0.1:8000/app-coder/estudiante-formulario/`, nos devuelve un formulario para crear un nuevo estudiante.
    Al ingresar, siguiendo el ejemplo: `http://127.0.0.1:8000/app-coder/profesor-formulario/`, nos devuelve un formulario para crear un nuevo estudiante.
    Al ingresar, siguiendo el ejemplo: `http://127.0.0.1:8000/app-coder/busquedaCamada/`, nos devuelve un formulario para realizar una busqueda por camada. Si encuentra informacion de la busqueda la muestra en el endpoint `http://127.0.0.1:8000/app-coder/buscar/?csrfmiddlewaretoken=hash` el resultado de la misma.
    