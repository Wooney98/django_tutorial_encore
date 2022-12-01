from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm


class UserCreateView(CreateView):
    form_class = CreateUserForm # forms.py에 정의되어있는 form 클래스
    template_name = 'registration/register.html' # 랜더링할 템플릿 파일
    # 폼에 입력된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정함.
    #success_url = 'done/'
    success_url = reverse_lazy('register_done') # url패턴 전달인자, urls.py 모듈이 메모리 로딩된 후 실행

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'