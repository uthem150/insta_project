from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta: #Meta 클래스를 내부 클래스로 정의하여 폼의 동작과 속성을 설정
        model = Project #폼과 연결할 데이터 모델을 Project로 지정
        fields = ['image', 'title', 'description'] #폼에서 사용할 필드들을 지정