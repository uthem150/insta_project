from django.urls import path

from projectapp.views import ProjectListView, ProjectCreateView, ProjectDetailView

app_name = 'projectapp'

#URL 패턴을 정의하고 해당 URL 패턴과 처리할 view 함수를 연결

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='list'), #"/list/" 경로에 접속하면 ProjectListView 클래스 인스턴스를 생성하여 뷰 처리, name 매개변수를 통해 해당 URL 패턴에 'list'라는 이름 부여(이 이름은 다른 곳에서 해당 URL 패턴을 참조할 때 사용)

    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'), #"/detail/int:pk" 경로에 접속하면 ProjectDetailView 클래스의 인스턴스를 생성하여 뷰를 처리
]