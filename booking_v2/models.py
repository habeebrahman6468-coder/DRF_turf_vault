from django.db import models

from turf.models import Turf

# Create your models here.


class Booking(models.Model):

    customer_name = models.CharField(max_length=200)

    contact_no = models.CharField(max_length=15)

    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    reservation_date = models.DateField()

    reservation_time = models.TimeField(
        editable=False,
        null=True
    )

    end_time =models.TimeField()

    duration = models.DurationField(max_length=200)

    def __str__(self):
        return self.customer_name