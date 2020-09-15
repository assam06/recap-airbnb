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

    """ RoomType Model Definition"""

    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    # 이름 변경하는 코드
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()

    # 파이썬은 파일을 상하수직방향으로 읽음. ""(string)을 하지 않으면 장고는 Room(모델)을 정의 못해.
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )

    # 방의 타입은 roomtype중 한 종류여야해. 여러객실 유형이어선 안돼.
    # 객실 유형은 한가지 또는 다른유형 그리고 삭제하는 경우엔 Room을 삭제해선 안돼.
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    # 이걸 써줘야 등록한 이름이 나옴....흠
    # 생성된 obj or model을 지칭하는 것을 뭘로 설정할거야? 의 의미
    def __str__(self):
        return self.name