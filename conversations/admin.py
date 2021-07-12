from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    
    list_display = [
        "__str__",
        "count_msg",
        "count_participant",
    ]


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    
    list_display = [
        "__str__",
        "created",
    ]
