from django.http import HttpResponseForbidden

from articleapp.models import Article

def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        article = Article.objects.get(pk=kwargs['pk']) #Article 객체의 작성자(writer)가 현재 요청한 사용자(request.user)와 일치하는지 확인
        if not article.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs) #일치하는 경우에는 func(request, *args, **kwargs)를 호출하여 원래의 함수를 실행
    return decorated