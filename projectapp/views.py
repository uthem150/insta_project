from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription

#클라이언트의 요청을 처리하고, 필요한 데이터를 모델로부터 가져와서 템플릿을 렌더링

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project #projectapp.models 모듈에서 정의되어 있는 Django의 모델과 연결
    form_class = ProjectCreationForm #폼으로 사용할 ProjectCreationForm을 지정
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        #새로운 프로젝트 생성 후, reverse 함수를 사용하여 'projectapp:detail' URL 패턴으로 리디렉션
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin): # 프로젝트 상세 정보를 보여주는 뷰 (Mixin을 사용해서 프로젝트 아래에 이미지 넣기)
    model = Project
    context_object_name = 'target_project' #템플릿에서 사용할 객체의 변수명을 설정
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    # 프로젝트 아래에, 게시글들이 나올 수 있도록
    def get_context_data(self, **kwargs):
        project = self.object #현재 객체를 가져옴
        user = self.request.user #현재 요청을 보낸 사용자를 가져옴
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project) #현재 사용자와 프로젝트에 대한 구독 객체를 필터링

        object_list = Article.objects.filter(project=self.get_object()) #Article 모델에서 project 필드가 현재 뷰의 get_object() 메서드에서 반환된 프로젝트와 일치하는 객체들을 필터링하여 저장
        #부모 클래스인 DetailView의 get_context_data() 메서드를 실행
        #이때, 추가로 전달할 컨텍스트 데이터인 object_list와 subscription을 함께 전달( 반환된 컨텍스트 데이터는 템플릿에서 사용)
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)

class ProjectListView(ListView): #프로젝트 목록을 보여주는 뷰
    model = Project
    context_object_name = 'project_list' #템플릿에서 사용할 객체의 변수명 설정
    template_name = 'projectapp/list.html' #template_name 속성을 사용하여 사용할 HTML 템플릿 파일을 지정
    paginate_by = 20 #paginate_by 속성을 사용하여 페이지당 보여줄 항목 수를 설정

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