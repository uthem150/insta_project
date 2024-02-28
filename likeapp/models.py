from django.contrib.auth.models import User
from django.db import models

from articleapp.models import Article


# Create your models here.

class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record') #user 필드는 User 모델과의 관계를 나타내는 외래 키, User 객체가 삭제되었을 때 Like 객체도 함께 삭제되도록 설정
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record') #Article 모델과의 관계를 나타내는 외래 키, Article 객체가 삭제되었을 때 Like 객체도 함께 삭제

    class Meta: #메타데이터를 정의 (모델의 동작이나 설정을 제어하는 데 필요한 정보를 담음)
        unique_together = ('user', 'article') #user와 article 필드의 값이 고유해야 함