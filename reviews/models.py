from django.db import models
from django.db.models.deletion import CASCADE

from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    review = models.CharField(max_length=400)
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    locations = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    user = models.ForeignKey("users.User",related_name= "reviews", on_delete=CASCADE)
    room = models.ForeignKey("rooms.Room",related_name= "reviews", on_delete=CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"

    def review_avg(self):
        
        avg = (
            self.accuracy + 
            self.communication + 
            self.cleanliness + 
            self.locations + 
            self.check_in + 
            self.value
            ) / 6 

        return round(avg,2)
