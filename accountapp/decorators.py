from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs): #데코레이터로 감싸진 함수의 동작을 정의
        user = User.objects.get(pk=kwargs['pk']) #주어진 pk 값에 해당하는 사용자를 데이터베이스에서 가져옴
        if not user == request.user: #해당 사용자가 현재 요청을 보낸 사용자와 일치하는지 확인
            return HttpResponseForbidden() #일치하지 않을 경우 HttpResponseForbidden()를 반환하여 403 Forbidden 응답을 전송
        return func(request, *args, **kwargs)
    return decorated