from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input') #request에서 post메소드 중에서 hello_world_input이라는 이름을 가진 데이터를 가져오기

        new_hello_world = HelloWorld() #models.py의 HelloWorld에서 나온 새로운 객체가 저장됨.
        new_hello_world.text = temp #텍스트 필드 안에 받은 값 넣어주기
        new_hello_world.save() #db에 데이터를 저장시키고 있음.

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world}) #accountapp 폴더 내부의 hello_world파일 가져오기 (header, footer는 변하지x)
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
