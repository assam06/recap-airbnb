from django.contrib.auth.models import AbstractUser
from django.db import models

# data 변경하는 곳(models.py)
# 이 AbstractUser도 장고의 베이직에서 갖고온거. 그럼 User가 AbstractUser의 성격을 상속하겠지ㅎㅎ
class User(AbstractUser):

    pass