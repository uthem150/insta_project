from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

@login_required
def hello_world(request):

    if request.user.is_authenticated: #로그인을 해야만, 게시글을 볼 수 있도록
        if request.method == "POST":

            temp = request.POST.get('hello_world_input') #request에서 post메소드 중에서 hello_world_input이라는 이름을 가진 데이터를 가져오기

            new_hello_world = HelloWorld() #models.py의 HelloWorld에서 나온 새로운 객체가 저장됨.
            new_hello_world.text = temp #텍스트 필드 안에 받은 값 넣어주기
            new_hello_world.save() #db에 데이터를 저장시키고 있음.

            return HttpResponseRedirect(reverse('accountapp:hello_world')) #reverse('accountapp:hello_world')는 Django에서 URL 패턴 이름을 기반으로 해당 URL을 생성하는 함수
        else:
            hello_world_list = HelloWorld.objects.all()  # 모든 HelloWorld 객체들을 불러옴
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) #accountapp 폴더 내부의 hello_world파일 가져오기 (header, footer는 변하지x)
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

# 장고의 제너릭에 있는 CreateView를 상속받아서 사용
class AccountCreateView(CreateView) :
    model = User #모델을 생성하는 데 사용될 모델 클래스를 지정
    form_class = UserCreationForm # UserCreationForm을 사용하여 사용자 생성에 필요한 입력 폼을 정의
    success_url = reverse_lazy('accountapp:hello_world') #폼 제출 후에 이동할 URL을 지정
    template_name = 'accountapp/create.html' #사용될 템플릿 파일의 경로를 지정 (회원가입을 할 때 볼 html파일)

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25
    # mypage아래에 나의 게시글들 가져오기
    def get_context_data(self, **kwargs): #부모 클래스의 get_context_data 메서드를 실행
        object_list = Article.objects.filter(writer=self.get_object()) #Article 모델에서 writer 필드가 현재 뷰의 get_object() 메서드에서 반환된 작성자와 일치하는 객체들을 필터링하여 저장
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs) #부모 클래스의 get_context_data 메서드에 전달

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView) :
    model = User #모델을 생성하는 데 사용될 모델 클래스를 지정
    context_object_name = 'target_user'
    form_class = AccountUpdateForm # UserCreationForm을 사용하여 사용자 생성에 필요한 입력 폼을 정의
    success_url = reverse_lazy('accountapp:hello_world') #폼 제출 후에 이동할 URL을 지정
    template_name = 'accountapp/update.html' #사용될 템플릿 파일의 경로를 지정


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
