from django.db import models
from django.contrib.gis.db import models as geo
from passenger.models import Passenger
from driver.models import Driver


TRIP_STATE_CHOICES = [
    ('pending', 'Pending'),
    ('in_course', 'In course'),
    ('finished', 'Finished')
]

class Trip(models.Model):
    origin = geo.PointField(srid=4326,blank=False, null=False)
    destination = geo.PointField(srid=4326,blank=True,null=True)
    distance = models.FloatField()
    state= models.CharField(choices=TRIP_STATE_CHOICES, default='pending', max_length=20)
    begin_time = models.DateTimeField(null=True)
    finish_time= models.DateTimeField(null=True)
    duration= models.TimeField(null=True)
    passenger= models.ForeignKey(Passenger, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)

class CityBoundary(models.Model):
    name = models.CharField(max_length=255)
    boundary= geo.MultiPolygonField(srid=4326)
    
    def __str__(self) -> str:
        return f"The model belongs to {self.name}, id={self.id}"
    