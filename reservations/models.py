from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    # 예약 상태 넣을거야

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_PENDING, "Confirmed"),
        (STATUS_PENDING, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # 아... self가 reservation이라고 나오네? class 내의 self라서 그런가봐!
    def __str__(self):
        return f"{self.room} - {self.check_in}"

    # 현재 날짜가 체크인날짜보다 큰지 체크아웃 날짜보다 적은지 체크
    # time zone 필요해(import)_ 나라별 시간도(app의 서버시간) 체크해야하니까 timezone쓰는거임
    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    # 여기까지하면 in progress는 False/True일거야
    # 얘로 O X가 됨
    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
