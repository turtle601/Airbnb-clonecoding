from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField

from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICE = [
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    ]

    status = models.CharField(max_length=12, choices=STATUS_CHOICE)
    check_in = DateField()
    chekc_out = DateField()

    guest = models.ForeignKey("users.User", on_delete=CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
