from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):

    if request.method == "POST":
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!'}) #accountapp 폴더 내부의 hello_world파일 가져오기 (header, footer는 변하지x)
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
