from django.urls import path

from profileapp.views import ProfileCreateView

app_name = 'profileapp' #해당 앱의 이름을 정의

urlpatterns = [ #URL 패턴들을 정의하는 리스트
    path('create/', ProfileCreateView.as_view(), name='create'), #/create/ 경로에 대한 URL 패턴 정의('create/'은 http://도메인주소/create/에 해당하는 URL)
]