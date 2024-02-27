from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model): #models.Model을 상속받아 Comment 모델을 생성
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment') #Comment가 어떤 Article과 연결되어 있는지를 나타냄 Article이 삭제되었을 때 Comment의 article 필드를 NULL로 설정
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment') #Comment를 작성한 User를 나타냄. User가 삭제되었을 때 Comment의 writer 필드를 NULL로 설정

    content = models.TextField(null=False) #댓글의 내용을 저장하는 필드(NULL 값을 허용하지 않음)

    created_at = models.DateTimeField(auto_now=True) #댓글이 생성될 때마다 자동으로 현재 시간으로, 댓글이 생성된 시간을 저장


#Comment 모델을 정의하는 부분. Comment 모델은 models.Model을 상속받아 생성
#article: Article 모델과의 관계를 나타내는 외래키. Article과 연결되어 있으며, Article이 삭제되면 Comment의 article 필드는 NULL로 설정
#writer: User 모델과의 관계를 나타내는 외래키. User와 연결되어 있으며, User가 삭제되면 Comment의 writer 필드는 NULL로 설정.
#content: 댓글의 내용을 저장하는 필드. NULL 값을 허용하지 않음.
#created_at: 댓글이 생성된 시간을 저장하는 필드, 댓글이 생성될 때마다 자동으로 현재 시간으로 설정.

#이렇게 정의된 Comment 모델은 데이터베이스에 해당하는 테이블로 생성되며, commentapp 앱 내에서 댓글 데이터를 저장하고 관리하는 역할을 수행