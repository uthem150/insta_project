"""
URL configuration for instagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path: Django URL 패턴을 정의하는 함수  (URL 패턴, 해당 URL 패턴에 매치될 때 실행될 뷰 함수나 include 함수)
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')), #accounts라는 주소로 접근하면, account app으로 접근
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')), #사용자가 'comments/' URL에 접근했을 때, 'commentapp' 애플리케이션의 URL 설정을 참조
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #instagram폴더 settings안에 적은 값을 가져옴
