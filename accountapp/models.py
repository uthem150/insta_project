from django.db import models

# Create your models here.

# Django에서 모델은 데이터베이스 테이블과의 상호작용을 관리하는데 사용되는 객체 (데이터베이스에 저장될 데이터)
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) #문자열 필드, 최대 길이 255, 필드가 비어 있을 수 없음
