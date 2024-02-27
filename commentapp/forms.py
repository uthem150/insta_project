from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreationForm(ModelForm):
    class Meta: #메타데이터를 설정
        model = Comment #Comment 모델과 연결되어 있음(CommentCreationForm은 Comment 모델과 관련된 데이터를 입력받는 용도로 사용됨)
        fields = ['content'] #'content' 필드만 입력받을 수 있도록 설정