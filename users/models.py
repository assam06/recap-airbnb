from django.contrib.auth.models import AbstractUser
from django.db import models

# data 변경하는 곳(models.py)
# 이 AbstractUser도 장고의 베이직에서 갖고온거. 그럼 User가 AbstractUser의 성격을 상속하겠지ㅎㅎ
# 이 모델을 admin.py에 연결할거야 (User)
# 3.1 여기다가 뭘 적든 장고가 form을 만들어 줄거야. 그리고 장고는 db에다가 migration이랑 같이 form에 필요한 정보를 요청할거야
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        # DB로 가는 것       #Form에 나타는 글자
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    # 사진 추가할거야 (avatar)
    # CharField는 원래 인자1개 필요한 애야.그리고 비어있는거 허용해줌, 그리고 choices 적용 가능해
    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)