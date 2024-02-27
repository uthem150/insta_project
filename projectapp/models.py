from django.db import models

# Create your models here.

# 데이터베이스 테이블과 매핑되는 모델 클래스를 작성
class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)