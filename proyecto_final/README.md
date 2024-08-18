# TecnoStore tienda online con Django README

## Descripción
Proyecto orientado al desarrollo web, realizado con Django como framework para el backend, SQlite para base de datos, HTML, CSS, javascript y bootstrap para el frontend.
Esta aplicacion permite al usuario registrarse, logearse y modificar su perfil. En dicho perfil una vez logueado, puede modificar sus datos y agregar un avatar personalizado si asi lo quisiera y sino es asignado un avatar por defecto.
Tambien el usuario puede acceder desde el navbar a la tienda de productos donde el usuario puede ver los productos ordenados segun sean agregados por el administrador y paginados cada diez productos por pagina. Cada producto tiene titulo, descripcion, precio y un boton de "ver" que nos lleva a una pagina con el detalle del mismo.
Una de las cosas que mas destacas al haber sido desarrollado con django es que tiene un panel de administrador, donde el usuario administrador puede hacer las modificaciones tanto de productos como de usuarios.

## Requisitos
- Python 3.x
- Django 5.x
- pillow 10.x
- Virtualenv (opcional pero recomendado)

### Instalacion y uso
1. Clona el repositorio:
    ```sh
    git clone https://github.com/cristianobus0909/python_web.git
    cd proyecto_final
    ```

2. Crea y activa un entorno virtual:
    ```sh
    pipenv shell
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

5. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver

6. Abre tu navegador y visita http://localhost:8000.