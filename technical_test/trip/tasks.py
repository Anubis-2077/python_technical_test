from celery import shared_task
from driver.models import Driver
from passenger.models import Passenger
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D


@shared_task
def update_available_drivers():
    #obtain waiting passengers
    waiting_passengers = Passenger.objects.filter(state='waiting')
    
    for passenger in waiting_passengers:
        #find nearby drivers
        nearby_drivers = Driver.objects.filter(
            state = 'available',
            location_distance_lte = (passenger.location, D(km=5))
        ).annotate(
            distance = Distance('location', passenger.location)
        ).order_by('distance')