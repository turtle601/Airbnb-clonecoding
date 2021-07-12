from django.db import models
from django.db.models.fields import CharField

from django_countries.fields import CountryField

from core import models as core_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = CharField(max_length=40)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]

    pass


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"

    pass


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"

    pass


class Photo(core_models.TimeStampedModel):
    """Photo Modle Definition"""

    caption = CharField(max_length=40)
    file = models.ImageField(upload_to = "rooms_photos")
    room = models.ForeignKey("Room", related_name= "photos" ,on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):
    """Room model definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", related_name = "rooms", on_delete=models.CASCADE)
    room_type = models.ManyToManyField("RoomType", related_name = "rooms", blank=True)
    amenities = models.ManyToManyField("Amenity", related_name = "rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name = "rooms", blank=True)
    house_rule = models.ManyToManyField("HouseRule", related_name = "rooms", blank=True)

    def __str__(self):
        return self.name

    def room_review_avg(self):
        sum = 0

        reviews = self.reviews.all()       

        for review in reviews:
            sum += review.review_avg()

        return sum / len(reviews)