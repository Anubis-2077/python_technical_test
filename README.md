# Ride Assignment Application

This project simulates a ride assignment system for a ride-hailing application, similar to Uber, focusing on optimizing driver assignments and managing city boundaries.

## Table of Contents

1. Project Overview

2. Setup and Installation

3. Running the Application

4. Custom Commands

5. Tes5ting

6. Notes

### Project Overview

This project is divided into three Django applications:

trip: Manages ride requests and assignments.

passenger: Handles passenger data and requests.

driver: Manages driver data and availability.

### Key Libraries

Django: Version 4.2.16

psycopg2-binary: Version 2.9.9

GDAL: Version 3.6.3

### Setup and Installation

1. Clone the Repository

git clone https://github.com/Anubis-2077/python_technical_test.git
cd technical_test

2. Build and Start Containers Make sure Docker and Docker Compose are installed. Build and start the containers with:

docker-compose up --build

3. Verify Services Ensure that the following services are running:

Django application
PostgreSQL database with PostGIS extension

### Running the Application
Once the containers are running, you can access the Django application at http://localhost:8000.

### Custom Commands

Initialize City Boundary Data
To set up initial city boundary data for New York, use the custom management command:

docker-compose exec django python manage.py create_nyc

### Database Migrations

Apply database migrations with:

docker-compose exec web python manage.py migrate

### Testing
To run tests, use the following command:

docker-compose exec web python manage.py test

Ensure that your tests include scenarios for:

Driver and passenger location validation
Ride assignment logic

### Notes

Celery and Redis: Integration with Celery and Redis is prepared but not currently active. These can be implemented as needed for asynchronous task processing.

Configuration: Adjust settings in the technical_test/settings.py file if necessary to match your environment.

Troubleshooting: If you encounter issues, check the logs with docker-compose logs for more details.