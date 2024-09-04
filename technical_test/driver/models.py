from django.db import models
from django.contrib.gis.db import models as geo

STATE_CHOICES = [
    ('available', 'Available'),
    ('unavailable', 'Unavailable'),
    ('on_trip', 'On Trip'),
    ('occupied', 'Occupied')
]


class Driver(models.Model):
    name = models.CharField(max_length=100)
    car = models.CharField(max_length=50)
    state = models.CharField(choices=STATE_CHOICES, default='available', max_length=20)
    location= geo.PointField(srid=4326,null=True, blank=True)
    
    class Meta:
        indexes = [
            geo.Index(fields=['location'], name='location_idx_driver')
        ]
    
