from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms


# UserCreatioForm을 상속받은 새로운, 사용자 정보 업데이트 폼을 정의하는 클래스
class AccountUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']  # 필요한 필드만 포함하도록 수정
    def __init__(self, *args, **kwargs): #__init__ 메서드를 오버라이드하여 폼이 초기화될 때 실행되는 동작을 정의
        super().__init__(*args, **kwargs) #  부모 클래스인 UserCreationForm의 __init__ 메서드를 실행

        self.fields['username'].disabled = True #username 필드를 비활성화

    def clean_username(self):
        # username 필드를 변경하지 않도록 유효성 검사를 추가
        username = self.instance.username
        if self.cleaned_data['username'] != username:
            raise forms.ValidationError('Cannot change username')
        return username
