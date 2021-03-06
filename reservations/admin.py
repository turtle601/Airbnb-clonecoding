from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    
    list_display= [
        "status",
        "check_in",
        "check_out",
        "guest",
        "room", 
        "in_progress",
        "is_finished",
    ]
