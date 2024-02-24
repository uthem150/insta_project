from django.contrib.auth.forms import UserCreationForm

# UserCreatioForm을 상속받은 새로운, 사용자 정보 업데이트 폼을 정의하는 클래스
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs): #__init__ 메서드를 오버라이드하여 폼이 초기화될 때 실행되는 동작을 정의
        super().__init__(*args, **kwargs) #  부모 클래스인 UserCreationForm의 __init__ 메서드를 실행

        self.fields['username'].disabled = True #username 필드를 비활성화