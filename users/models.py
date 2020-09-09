from django.contrib.auth.models import AbstractUser
from django.db import models

# data 변경하는 곳(models.py)
# 이 AbstractUser도 장고의 베이직에서 갖고온거. 그럼 User가 AbstractUser의 성격을 상속하겠지ㅎㅎ
# 이 모델을 admin.py에 연결할거야 (User)
# 3.1 여기다가 뭘 적든 장고가 form을 만들어 줄거야. 그리고 장고는 db에다가 migration이랑 같이 form에 필요한 정보를 요청할거야
class User(AbstractUser):

    bio = models.TextField(default="")