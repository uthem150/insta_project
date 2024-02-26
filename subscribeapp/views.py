from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription

#클라이언트의 요청을 처리하고, 필요한 데이터를 모델로부터 가져와서 템플릿을 렌더링

@method_decorator(login_required, 'get') #로그인해야 구독할 수 있도록
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')}) #리디렉션할 URL을 반환

    def get(self, request, *args, **kwargs): #HTTP GET 요청을 처리하는 메서드
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) #'project_pk' 값을 사용하여 Project 모델에서 해당 프로젝트를 가져옴
        user = self.request.user #현재 요청의 사용자를 가져옴
        subscription = Subscription.objects.filter(user=user, project=project) #Subscription 모델에서 user와 project 필드가 주어진 사용자와 프로젝트에 해당하는 구독을 필터링한 결과를 반환

        if subscription.exists(): #구독 객체가 존재하는지 확인
            subscription.delete() #subscription.delete()를 호출하여 구독을 취소
        else:
            Subscription(user=user, project=project).save() #Subscription 모델을 생성하여 사용자와 프로젝트를 연결하고 저장
        return super(SubscriptionView, self).get(request, *args, **kwargs) #부모 클래스인 RedirectView의 get 메서드를 실행합니다