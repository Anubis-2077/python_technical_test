FROM postgres:14  

# Actualiza el sistema de paquetes
RUN apt-get update && apt-get install -y postgis postgresql-14-postgis-3

ENV POSTGRES_USER=Anubis
ENV POSTGRES_PASSWORD='123'
ENV POSTGRES_DB=trip_app_db

COPY init-db.sh /docker-entrypoint-initdb.d/

RUN echo "CREATE EXTENSION postgis;" >> /docker-entrypoint-initdb.d/init-db.sh
