from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article', null=True) #탈퇴를 해도 게시글이 사라지지 않고, 주인없음 형태로 남도록
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True) #탈퇴를 해도 프로젝트가 사라지지 않고, 주인없음 형태로 남도록

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

    # like = models.IntegerField(default=0) #좋아요 수
    liked_users = models.ManyToManyField(User, related_name='liked_articles', blank=True)  # 좋아요를 누른 사용자를 저장하는 ManyToManyField


