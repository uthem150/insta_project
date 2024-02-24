from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk']) # kwargs에서 'pk'라는 키에 해당하는 값을 사용하여 Profile 모델에서 해당 프로필을 가져옴
        if not profile.user == request.user: #프로필의 소유자가 현재 요청을 보낸 사용자와 일치하지 않는 경우를 확인
            return HttpResponseForbidden() #일치하지 않을 경우 HttpResponseForbidden()을 반환
        return func(request, *args, **kwargs) #일치하는 경우에는 func(request, *args, **kwargs)를 호출하여 데코레이터를 적용한 함수의 기능을 수행
    return decorated