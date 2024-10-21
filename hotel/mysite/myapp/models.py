from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room_id = models.IntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Booking {self.id} for {self.client}'