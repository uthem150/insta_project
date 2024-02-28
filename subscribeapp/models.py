from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project

# 데이터베이스 테이블과 매핑되는 모델 클래스를 작성

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription') #models.ForeignKey를 사용하여 User 모델과의 관계를 설정(on_delete=models.CASCADE는 사용자가 삭제될 경우 해당 구독도 함께 삭제되도록 설정)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription') #models.ForeignKey를 사용하여 Project 모델과의 관계를 설정(프로젝트가 삭제될 경우 해당 구독도 함께 삭제되도록 설정한 것)

    class Meta:
        unique_together = ('user', 'project') #unique_together 속성. user와 project 필드의 값이 고유해야 함(동일한 사용자와 프로젝트에 대한 중복 구독을 방지)