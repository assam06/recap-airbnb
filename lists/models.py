# 리스트는 이름/장소로 구성됨
from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """List Model Definition """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)

    def __str__(self):
        return self.name