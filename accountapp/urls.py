from django.urls import path #패턴을 설정하는 함수

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

# "127.0.0.1:8000/account/hello_world"
# "accountapp:hello_world" -> accountapp내부에서 hello_world라는 이름의 주소로 바로 가라

urlpatterns = [
    path('hello_world/', hello_world, name="hello_world"), #URL 패턴으로 사용할 경로, URL 패턴에 대해 호출될 함수 또는 뷰, 이 URL 패턴의 이름을 "hello_world"로 지정
    path('create/', AccountCreateView.as_view(), name="create"), #회원가입 경로 지정 (class based view는 함수형처럼 작동하게 하려면, as_view()붙여야 함)
]