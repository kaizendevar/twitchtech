# Twitch Tech

Stack: Python 3.8 y Django.

Listado de vivos en Español en este momento sobre Ciencia y Tecnología en la Plataforma Twitch

  - [x] Solo muestra el Título del Stream.
  - [x] Devuelve un HTML simple, sin formato.
 
Estoy haciendo un reto de 7 días de MVP's de diferentes tecnologías: [@martindevaluado](http://twitter.com/martindevaluado)

![Primer diseño](https://i.imgur.com/5xj7WYJ.jpg)

# Próximas características

  - [ ] Añadir CSS.
  - [ ] Al hacer clic en el título poder ver el Stream (iframe) sin salir de la página.


Para ejecutar:

- Instalar Python
- Instalar Django
- Instalar requests

Como utilizo Visual Studio Code seguí este [tutorial](https://code.visualstudio.com/docs/python/tutorial-django)

Modificar views.py
Líneas 13 y 14 haciendo los siguientes pasos:

```sh
Obtener client-id y authorization creando Aplicación en https://dev.twitch.tv/console/apps
Luego hacer un POST como el siguiente para tener el TOKEN:
POST https://id.twitch.tv/oauth2/token?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=client_credentials
```

Levantar servidor:

```sh
python manage.py runserver
```
