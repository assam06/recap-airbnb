from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        # conversation을 만들었는데 내 str이 string이 아니어서 self.created에 ()주고 앞에 str을 붙였어
        return str(self.created)


class Message(core_models.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversations = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.text}"
