from .models import *

Flights.objects.all()

departure_airport__departure_code = 'LED'

Flights.objects.all().filter(departure_airport__airport_code='LED')

Seats.objects.all().filter(aircraft_code__seats_no='*')

Boarding_passes.objects.all().filter(flight_id='202B')

Tickets.objects.all().filter(passenger_name='*')