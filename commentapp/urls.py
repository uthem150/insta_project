from django.urls import path

from commentapp.views import CommentCreateView, CommentDeleteView

app_name = 'commentapp' #앱의 이름인 "commentapp"을 지정

urlpatterns = [ #URL 패턴들을 설정
    path('create/', CommentCreateView.as_view(), name='create'), #"/create/" 경로로 접근하는 요청을 CommentCreateView 뷰와 연결하여 처리하도록 설정
    path('delete/<int:pk>', CommentDeleteView.as_view(), name='delete'),
    #name='delete'를 사용하면 다른 곳에서 해당 URL 패턴을 참조할 때,
    #예를 들어 템플릿에서 URL을 생성하거나 뷰에서 reverse('delete')를 사용하여 URL을 역으로 찾을 때 사용
]