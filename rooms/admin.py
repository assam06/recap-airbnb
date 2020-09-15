from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


# 모델이 외부에서 보여지는 방식(리스트처럼) 과 안에서 보이는 방식을 변경해
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        ("Basic Info", {"fields": ("name", "description", "country", "city", "price")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Space",
            {  # 접는 섹션
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")

    # 기본적으로  ManytoMany로 작동함. 장고의 룰
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )
    # self는 class RoomAdmin이고 obj는 현재 row
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass