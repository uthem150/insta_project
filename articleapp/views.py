from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView): #게시글 생성에 대한 뷰를 정의 (CreateView를 상속받아 게시글 생성에 대한 뷰를 정의하는 클래스)
    model = Article #이 뷰가 Article 모델과 연결되어 있음
    form_class = ArticleCreationForm #해당 뷰에서 사용할 폼 클래스를 지정
    template_name = 'articleapp/create.html' #뷰에서 사용할 템플릿 파일의 경로를 지정

    def form_valid(self, form): #폼 데이터가 유효할 때 호출되는 메서드(폼 데이터를 저장하기 전에 추가적인 작업)
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user #현재 요청을 보낸 사용자를 할당하고, 게시글을 저장
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self): #게시글 생성이 성공한 후 이동할 URL을 반환하는 메서드
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

# 다중상속을 위해 FormMixin
class ArticleDetailView(DetailView, FormMixin): #Article 모델의 상세보기 기능을 구현
    model = Article #model 변수에 Article 모델을 연결하여 해당 모델의 객체를 가져옴
    form_class = CommentCreationForm
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


class ArticleListView(ListView): #ListView를 상속받은 ArticleListView 클래스를 정의
    model = Article
    context_object_name = 'article_list' #템플릿에서 사용할 컨텍스트 변수의 이름, article_list라는 이름으로 템플릿에 전달
    template_name = 'articleapp/list.html'
    paginate_by = 7 #한 페이지에 보여줄 항목의 수

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')  # 게시글을 가장 최신 순으로 정렬해서 가져옴

    def get_context_data(self, **kwargs): #ListView가 템플릿에 전달하는 컨텍스트 데이터를 추가로 제공하거나 수정
        context = super().get_context_data(**kwargs) #부모 클래스인 ListView의 get_context_data 메소드를 호출하여 기본 컨텍스트 데이터를 가져옴
        total_pages = context['paginator'].num_pages # 페이징 처리를 위해 전체 페이지 수를 total_pages 변수에 저장
        current_page = context['page_obj'].number #현재 페이지 번호를 current_page 변수에 저장

        # 페이지 그룹의 시작 페이지와 끝 페이지를 계산합니다.
        start_page = ((current_page - 1) // 10) * 10 + 1
        end_page = start_page + 9
        if end_page > total_pages: #만약 끝 페이지 번호가 전체 페이지 수를 초과하면, 끝 페이지 번호를 전체 페이지 수로 수정
            end_page = total_pages

        context['page_range'] = range(start_page, end_page + 1) #시작 페이지부터 끝 페이지까지의 범위를 page_range라는 이름으로 컨텍스트 데이터에 추가
        return context #수정한 컨텍스트 데이터를 반환