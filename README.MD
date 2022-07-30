# Microservicio pruebaGS.
Demo desarrollada para prueba tecnica.
## Requisitos.
- Contar con python 3.10.5
- Contar con MongoDB 5.0.10 o superior.
- Editor de Swagger.

## Crear el entorno virtual (Windows).
```
py -3 -m venv venv
```
## Activar el entorno virtual (Windows).
```
. venv/Scripts/activate
```
## Instalacion de dependencias.
```
pip install -r requirements.txt
```
## Variables de entorno.
```
FLASK_APP=main.py
FLASK_ENV=development
MONGO_URI='mongodb://localhost:27017/registries'
```
## Ejecutar el proyecto.
```
flask run
```
## Visualizacion de la documentacion.
Usando la url: https://editor.swagger.io/ puedes importar el archivo alojado en la carpeta raiz con el nombre **swagger**.

### Librerias usadas
- Flask
- flask-cors
- Flask-PyMongo
- pymongo[srv]

Se pueden instalar de la siguiente forma:
```
pip install Flask
pip install -U flask-cors
pip install Flask-PyMongo
pip install "pymongo[srv]"
```
