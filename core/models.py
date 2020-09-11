from django.db import models


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # for extra info
    # abstract 모델은 모델이지만 DB에는 나타나지 않는 모델이야.
    class Meta:
        abstract = True