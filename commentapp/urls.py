from django.urls import path

from commentapp.views import CommentCreateView

app_name = 'commentapp' #앱의 이름인 "commentapp"을 지정

urlpatterns = [ #URL 패턴들을 설정
    path('create/', CommentCreateView.as_view(), name='create'), #"/create/" 경로로 접근하는 요청을 CommentCreateView 뷰와 연결하여 처리하도록 설정
]