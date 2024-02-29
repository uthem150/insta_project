from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Profile(models.Model): #데이터베이스에 저장될 필드들을 정의
    # User 모델과의 일대일 관계를 나타냄
    # #연결된 User 객체가 삭제될 경우 Profile 객체도 함께 삭제되도록 설정, User 객체에서 Profile 객체에 역참조할 때 사용할 이름을 정의
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/', null=True) #upload_to 매개변수는 이미지가 저장될 경로를 지정
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
