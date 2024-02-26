from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path #패턴을 설정하는 함수

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

# "127.0.0.1:8000/account/hello_world"
# "accountapp:hello_world" -> accountapp내부에서 hello_world라는 이름의 주소로 바로 가라

urlpatterns = [

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name="create"), #회원가입 경로 지정 (class based view는 함수형처럼 작동하게 하려면, as_view()붙여야 함)
    path('detail/<int:pk>', AccountDetailView.as_view(), name="detail"), #pk라는 int형 변수를 추가적으로 detail/다음에 받겠다는 의미.
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]