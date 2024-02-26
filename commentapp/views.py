from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment
from django.utils.decorators import method_decorator
from commentapp.decorators import comment_ownership_required


class CommentCreateView(CreateView):
    model = Comment #model 속성은 Comment 모델을 사용
    form_class = CommentCreationForm #form_class 속성은 CommentCreationForm 폼을 사용
    template_name = 'commentapp/create.html'

    def form_valid(self, form): #form_valid 메서드를 오버라이드하여 폼 데이터를 처리
        temp_comment = form.save(commit=False) #CommentCreationForm으로부터 폼 데이터를 받아와서 임시 Comment 객체를 생성
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk']) #article_pk 값을 통해 해당 댓글이 속하는 Article 객체를 가져옴
        temp_comment.writer = self.request.user #댓글 작성자를 현재 요청한 사용자로 설정
        temp_comment.save() #임시 Comment 객체를 저장
        return super().form_valid(form) #상속받은 부모 클래스의 form_valid() 메서드를 호출 (폼 데이터를 저장하고 새로운 객체를 생성)

    def get_success_url(self): #댓글 생성 후 이동할 URL을 반환하는 메서드
        # URL을 역으로 생성하는 함수인 reverse()를 사용하여 특정 뷰의 URL을 생성하는 코드
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk}) #URL 패턴에 전달할 매개변수를 지정 ('pk'라는 매개변수에 self.object.article.pk 값을 전달)


# 해당 메서드가 실행되기 전에 장식자의 로직이 실행되어 추가적인 처리
# 장식자의 로직이 실행되어 댓글 소유권을 확인하고, 소유권이 없는 경우에는 403 Forbidden 응답이 반환
# 다른 사용자가 해당 댓글 삭제 URL을 알고 있어도 삭제를 시도할 수 없음
@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk}) #해당 pk를 가진 article로 돌아가라

#CommentCreateView는 댓글 생성에 관련된 뷰로, CreateView 클래스를 상속받아 구현 (다음과 같은 기능을 제공)
#model: Comment 모델을 사용함을 지정.
#form_class: CommentCreationForm 폼을 사용함을 지정.
#template_name: 해당 뷰에 대한 HTML 템플릿 파일의 경로를 지정.
#form_valid(): 폼 데이터가 유효할 때 호출되는 메서드를 오버라이드하여 원하는 동작을 정의.
#get_success_url(): 댓글 생성 후 이동할 URL을 반환하는 메서드를 오버라이드하여 원하는 URL을 반환.

#views.py 파일은 뷰 클래스들을 정의하여 요청을 처리하고, 필요한 데이터를 템플릿에 전달하는 역할을 수행