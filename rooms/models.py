# 장고에 대한걸 다 import
# 외부패키지(third-party apps) import, 그리고 내가 만든 패키지 import
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    # 카테고리만 다를 뿐 카테고리마다 전부 item이들어가서 만든거
    """ Abstract Item """

    # 1. 이름넣을 칸을 만듦
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# 1-1. 그 이름이 여기에 들어감
class RoomType(AbstractItem):
    pass


class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # Foreign Key는 연결이 필요해 - room이랑 user랑 연결함
    room_type = models.ManyToManyField(RoomType, blank=True)

    # 이걸 써줘야 등록한 이름이 나옴....흠
    def __str__(self):
        return self.name