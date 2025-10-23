# Create your models here.
from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='')
    
    def __str__(self):
        # return self.name
        return f'{self.name} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f"{self.name} - {self.booking_date}"
        