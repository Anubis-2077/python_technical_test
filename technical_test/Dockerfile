FROM osgeo/gdal:ubuntu-small-3.6.3

# Instalar Python y pip
RUN apt-get update && apt-get install -y python3-pip

# Establecer la variable de entorno GDAL
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH

# Instalación de GDAL y otras dependencias
RUN pip install gdal psycopg2-binary

WORKDIR /app

# Copiar el código del proyecto desde la carpeta local `technical_test` a /app/technical_test
COPY . /app

# Copiar los archivos de requerimientos a /app
COPY requirements.txt /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000 para el servidor de Django
EXPOSE 8000

# Comando por defecto para ejecutar Gunicorn y Celery
CMD ["sh", "-c", "gunicorn technical_test.wsgi:application --bind 0.0.0.0:8000 & celery -A technical_test.celery worker -l info"]