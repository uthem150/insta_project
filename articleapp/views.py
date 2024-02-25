from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView): #게시글 생성에 대한 뷰를 정의 (CreateView를 상속받아 게시글 생성에 대한 뷰를 정의하는 클래스)
    model = Article #이 뷰가 Article 모델과 연결되어 있음
    form_class = ArticleCreationForm #뷰에서 사용할 폼 클래스를 지정
    template_name = 'articleapp/create.html' #뷰에서 사용할 템플릿 파일의 경로를 지정

    def form_valid(self, form): #폼 데이터가 유효할 때 호출되는 메서드(폼 데이터를 저장하기 전에 추가적인 작업)
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user #현재 요청을 보낸 사용자를 할당하고, 게시글을 저장
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self): #게시글 생성이 성공한 후 이동할 URL을 반환하는 메서드
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView): #Article 모델의 상세보기 기능을 구현
    model = Article #model 변수에 Article 모델을 연결하여 해당 모델의 객체를 가져옴
    context_object_name = 'target_article' #템플릿에서 해당 객체에 접근할 때 사용할 변수명을 설정
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView): #Article 모델의 수정 기능을 구현
    model = Article
    context_object_name = 'target_article' #템플릿에서 해당 객체에 접근할 때 사용할 변수명을 설정
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html' #사용할 템플릿 파일을 지정 (해당 뷰에서 get() 메서드가 실행되어 렌더링될 때 사용)

    def get_success_url(self): #수정이 성공적으로 이루어진 후 이동할 URL을 설정
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView): #Article 모델의 삭제 기능을 구현
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html' #사용할 템플릿 파일을 지정