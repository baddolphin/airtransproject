from django.db import models


# Create your models here.


class Bookings(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateTimeField()
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return "{} - {}".format(self.book_ref,
                                self.book_date)


class Tickets(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.ticket_no,
                                self.passenger_name)


class Ticket_flights(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    flight_id = models.ForeignKey('Flights',
                                  on_delete=models.CASCADE)
    fare_conditions = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return "{} - {}".format(self.flight_id,
                                self.amount)


class Boarding_passes(models.Model):
    ticket_no = models.ForeignKey(Ticket_flights,
                                  on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flights',
                                  on_delete=models.CASCADE)
    boarding_no = models.CharField(max_length=3)
    seat_no = models.ForeignKey('Seats',
                                on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)

    def __str__(self):
        return "{} - {}".format(self.boarding_no,
                                self.seat_no)


class Airports(models.Model):
    airport_code = models.CharField(max_length=4, primary_key=True)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=35)
    coordinates = models.CharField(max_length=100)
    timezone = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.airport_name,
                                self.city)


class Flights(models.Model):
    flight_id = models.CharField(max_length=4, primary_key=True)
    flight_no = models.PositiveIntegerField()
    scheduled_departure = models.DateTimeField()
    scheduled_arrival = models.DateTimeField()
    departure_airport = models.ForeignKey('Airports',
                                          related_name='departure_airport',
                                          on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey('Airports',
                                        related_name='arrival_airport',
                                        on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    aircraft_code = models.ForeignKey('Aircrafts',
                                      on_delete=models.CASCADE)
    actual_departure = models.DateTimeField()
    actual_arrival = models.DateTimeField()

    def __str__(self):
        return "{} - {}".format(self.flight_no,
                                self.departure_airport,
                                self.scheduled_departure,
                                self.arrival_airport,
                                self.scheduled_arrival)


class Aircrafts(models.Model):
    aircraft_code = models.CharField(max_length=4, primary_key=True)
    model = models.CharField(max_length=20)
    range = models.PositiveIntegerField()

    def __str__(self):
        return "{} - {}".format(self.aircraft_code,
                                self.model,
                                self.range)


class Seats(models.Model):
    aircraft_code = models.ForeignKey(Aircrafts, on_delete=models.CASCADE)
    seat_no = models.CharField(max_length=3, primary_key=True)
    fare_conditions = models.ForeignKey(Ticket_flights,
                                        on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.aircraft_code,
                                self.seat_no,
                                self.fare_conditions)


departure_airport__departure_code = 'LED'
