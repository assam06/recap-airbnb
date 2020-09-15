from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    check_out = models.IntegerField()
    value = models.IntegerField()
    # 유저를 삭제하면 모델(리뷰)도 사라져야하지
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 그리고 리뷰는 객실이랑 연결되어 있지
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"  # self.room 자체가 str을 불러서 name을 안부른것.
        # room이라고 써도 장고는 foreignKey를 보고 접근을 허용할거야.
        # self.room.country라고 하면 그대로 출력.
        # 이게 다 foreign key를 정의해서 그럼.

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    # 줄임말로 작성
    rating_average.short_description = "Avg."
