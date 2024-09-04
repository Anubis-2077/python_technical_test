from django.db import models
from django.contrib.gis.db import models as geo

PASSENGET_STATE = [
    ('no_trip', 'No Trip'),
    ('waiting', 'Waiting'),
    ('on_trip', 'On_trip'),
    ('arrived', 'Arrived'),
]

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    location = geo.PointField(srid=4326, null=True, blank=True)
    state = models.CharField(max_length=10, choices=PASSENGET_STATE, default='no_trip')
    
    class Meta:
        indexes = [
            geo.Index(fields=['location'], name='location_idx'),
        ]