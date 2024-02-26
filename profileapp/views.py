from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.

class ProfileCreateView(CreateView): #CreateView를 상속받아 프로필 생성에 대한 뷰를 정의하는 클래스
    model = Profile
    context_object_name = 'target_profile' #템플릿에서 사용할 컨텍스트 객체의 이름을 지정
    form_class = ProfileCreationForm #뷰에서 사용할 폼 클래스를 지정
    success_url = reverse_lazy('articleapp:list') #프로필 생성이 성공한 후 이동할 URL을 지정
    template_name = 'profileapp/create.html' #뷰에서 사용할 템플릿 파일의 경로를 지정


    def form_valid(self, form):
        temp_profile = form.save(commit=False) #임시 데이터 저장
        temp_profile.user = self.request.user #temp_profile.user에 현재 요청을 보낸 사용자를 할당하고,
        temp_profile.save() #프로필을 저장
        return super().form_valid(form)

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'profileapp/update.html'