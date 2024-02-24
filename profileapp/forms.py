from django.forms import ModelForm

from profileapp.models import Profile

#프로필 생성을 위한 폼인 ProfileCreationForm을 정의
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message'] #폼에서 사용자에게 입력받을 필드들을 나타내는 리스트