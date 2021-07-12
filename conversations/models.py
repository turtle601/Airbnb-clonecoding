from django.db import models
from django.db.models.deletion import CASCADE

from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):

    participant = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []

        for user in self.participant.all():
            usernames.append(user.username)
        
        return ", ".join(usernames)
     
    def count_msg(self):
        
        return self.messages.count()

    count_msg.short_description = "Number of message"

    def count_participant(self):
        return self.participant.count()

    count_participant.short_description = "Number of Participant"    

class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=CASCADE)
    conversation = models.ForeignKey(Conversation, related_name = "messages", on_delete=CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
