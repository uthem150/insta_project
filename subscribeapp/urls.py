from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

#URL 패턴을 정의하고 해당 URL 패턴과 처리할 view 함수를 연결

urlpatterns = [
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]