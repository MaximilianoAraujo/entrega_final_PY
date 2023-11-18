# Proyecto de Gestión de Juegos, Consolas y Periféricos
Este proyecto, desarrollado con Django, ofrece una plataforma web para gestionar información relacionada con juegos, consolas y periféricos. Facilita a los usuarios la exploración, creación, edición y eliminación de datos asociados a estos elementos.

## Descripción General
El objetivo principal de este proyecto es proporcionar una herramienta versátil para la gestión de productos relacionados con el mundo de los videojuegos. La aplicación permite a los usuarios realizar las siguientes acciones:

* Explorar Juegos: Permite buscar juegos por nombre y ver detalles como descripción, género, precio, fecha de lanzamiento y más.

* Crear y Editar: Ofrece formularios intuitivos para agregar nuevos juegos, consolas y periféricos, así como actualizar la información existente.

* Eliminar: Proporciona la capacidad de eliminar juegos de forma segura.

## Instalación

Clonar el Repositorio:

* git clone https://github.com/tu-usuario/nombre-del-repositorio.git
  
 Instalar Dependencias:

* pip install -r requirements.txt

 Migraciones de Base de Datos:

* python manage.py migrate

 Crear Superusuario:

* python manage.py createsuperuser

 Iniciar el Servidor:

* python manage.py runserver

Visita http://127.0.0.1:8000/ para acceder a la aplicación.

## Uso

### Página "Sobre Mí"
Proporciona una descripción de la aplicación y sus objetivos actuales.
### Página "Editar Información"
Permite la edición de información relacionada con juegos, consolas y periféricos.
### Página "Crear Consola"
Facilita la creación de nuevos modelos de consolas con detalles como marca, modelo y precio.
### Página "Crear Juego"
Permite la creación de nuevos juegos, proporcionando información esencial como nombre, género, descripción, precio, fecha de lanzamiento y portada.
### Página "Crear Periférico"
Ofrece un formulario para agregar nuevos periféricos con detalles como nombre, categoría, descripción y precio.
### Página "Detalles"
Muestra información detallada sobre un juego específico, incluyendo nombre, portada (si está disponible), descripción, género, precio y fecha de lanzamiento.
### Página "Eliminar Juego"
Confirmación para eliminar un juego específico.
### Página "Inicio"
La página de inicio da la bienvenida a los usuarios.
### Página "Búsqueda de Juegos"
Permite buscar juegos por nombre y muestra una lista con enlaces a detalles, edición y eliminación.
