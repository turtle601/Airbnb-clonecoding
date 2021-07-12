from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("More About the Space", {"fields": ("amenities", "facilities", "house_rule")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        ("Last Details", {"fields": ("host",)}),
    )

    ordering = ("name", "price")

    list_display = [
        "name",
        "price",
        "address",
        "beds",
        "baths",
        "guests",
        "check_in",
        "host",
        "count_amenities",
        "count_photos",
        "room_review_avg",
    ]

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "city",
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
        "country",
    )

    search_fields = ("=city", "^host__username")

    filter_horizontal = (
        "room_type",
        "amenities",
        "facilities",
        "house_rule",
    )

    def count_amenities(self, obj):
        
        return obj.amenities.count()

    def count_photos(self, obj):
        
        return obj.photos.count()
        
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
