from .models import *

Flights.objects.all()

departure_airport__departure_code = 'LED'

Flights.objects.all().filter(departure_airport__airport_code='LED')
