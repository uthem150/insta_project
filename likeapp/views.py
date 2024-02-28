from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@transaction.atomic
def db_transaction(user, article):
    if LikeRecord.objects.filter(user=user, article=article).exists():  # exists() 메서드를 사용하여, 사용자와 게시글이 일치하는 기록이 이미 존재하는지 확인
        LikeRecord.objects.filter(user=user, article=article).delete()  # 이미 좋아요한 이력이 있다면 해당 이력을 삭제합니다.
        # article.like -= 1
        article.liked_users.remove(user)  # 사용자 객체를 liked_users에서 제거
        article.save()  # 좋아요 수를 1 감소시킨 후 데이터베이스에 저장합니다.
    else:
        LikeRecord(user=user, article=article).save()  # LikeRecord 모델 객체를 생성, save() 메서드를 호출하여 해당 객체를 데이터베이스에 저장
        # article.like += 1
        article.liked_users.add(user)  # 사용자 객체를 liked_users에 추가
        article.save()  # 변경된 좋아요 수를 데이터베이스에 저장


# Create your views here.
# @transaction.atomic
# def db_transaction(user, article):
#     if LikeRecord.objects.filter(user=user, article=article).exists():  # exists() 메서드를 사용하여, 사용자와 게시글이 일치하는 기록이 이미 존재하는지 확인
#        raise ValidationError('Like already exists')
#     else:
#         LikeRecord(user=user, article=article).save()  # LikeRecord 모델 객체를 생성, save() 메서드를 호출하여 해당 객체를 데이터베이스에 저장
#
#     article.like += 1
#     article.save()  # 변경된 좋아요 수를 데이터베이스에 저장


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(selfself, *args, **kwargs): #이 메서드는 사용자를 리다이렉트해야 할 URL을 반환 (kwargs는 "keyword arguments"의 약자)
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}) #kwargs를 사용하여 게시글의 pk(기본 키) 값을 받아와서 해당 게시글의 상세 페이지로 리다이렉트

    def get(self, *args, **kwargs): #GET 요청을 처리하는 메서드

        user = self.request.user #사용자 정보를 가져옴
        article = get_object_or_404(Article, pk=kwargs['pk']) #Article 모델에서 pk 값을 기반으로 해당 게시글을 가져옴

        db_transaction(user, article)

        return super(LikeArticleView, self).get(self.request, *args, **kwargs) #좋아요 기록이 존재하지 않는 경우에는 super()를 사용하여 기본 RedirectView의 get() 메서드를 호출하여 GET 요청을 처리