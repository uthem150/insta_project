from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),

    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'), #update/<int:pk> URL로 접속하면 ArticleUpdateView가 호출되어 해당 뷰에서 정의된 로직이 실행. 이를 통해 update.html 템플릿이 렌더링
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]