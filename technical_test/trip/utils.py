from django.contrib.gis.geos import Point
from trip.models import CityBoundary, Trip
from django.shortcuts import get_object_or_404
from driver.models import Driver
#from passenger.models import Passenger
from django.contrib.gis.db.models.functions import Distance


def is_within_city_boundary(location):
    """
    check if the friver/passenger location is within city boundary or not.
    
    :param location: Point object representing the driver/passenger's current location.
    :return: True if the location is within city boundary, False otherwise.
    """
    
    
    #obtain the limits of the city boundary from database
    city_boundary = get_object_or_404(CityBoundary, name="City of New York, New York, United States")
    
    if city_boundary.boundary.contains(location):
        #print("the passenger location is inside the city limits.")
        return True
    else:
        #print("the passenger location is outside the city limits")
        return False
    
def assign_driver_to_passenger(passenger, city_boundary):
    """
    asign drivers to passengers based on their location.
    :passenger: instance of Passenger model.
    :city_boundary: instance of CityBoundary model.
    :return: True if the driver is assigned to the passenger, False otherwise.
    """
    
    # Verificar si la ubicación del pasajero está dentro del límite de la ciudad
    if not city_boundary.boundary.contains(passenger.location):
        print("the passenger location is outside the city limits.")
        return False
    
    #find drivers state == available and within city boundary
    available_drivers = Driver.objects.filter(
        state='available',
        location__within=city_boundary.boundary
        ).annotate(
        distance = Distance('location', passenger.location)
    ).order_by('distance')
    
    if available_drivers:
        print("thoose are the available drivers", available_drivers)
    else:
        print("there are not available drivers")
    
    if available_drivers.exists():
        closest_driver = available_drivers[0]
        
        #asign the passenger and create the trip
        trip = Trip.objects.create(
            origin = passenger.location,
            destination = None,
            distance = 0,
            state = 'pending',
            passenger = passenger,
            driver = closest_driver
            )
        
        print("Driver assigned to passenger: ", closest_driver)
        print(f"trip created {trip.origin}, passenger: {trip.passenger.name}, driver: {trip.driver.name}")

        #change the state of driver and passenger
        closest_driver.state = 'on_trip'
        closest_driver.save()
            
        passenger.state = 'on_trip'
        passenger.save()
        
        return trip
    
    print("No drivers available in the city boundary.")
    return False
        
    
    