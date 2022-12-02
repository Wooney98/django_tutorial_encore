from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreateUserForm
from django.contrib.auth.mixins import AccessMixin


class UserCreateView(CreateView):
    form_class = CreateUserForm # forms.py에 정의되어있는 form 클래스
    template_name = 'registration/register.html' # 랜더링할 템플릿 파일
    # 폼에 입력된 내용에 에러가 없고, 테이블 레코드 생성이 완료된 후에 이동할 URL을 지정함.
    #success_url = 'done/'
    success_url = reverse_lazy('register_done') # url패턴 전달인자, urls.py 모듈이 메모리 로딩된 후 실행

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

#믹스인 클래스 추가
class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object"

    def dispatch(self, request, *args, **kwargs): # 소유자 여부 판단
        obj = self.get_object()                   # 대상이 되는 객체 가져오기
        if request.user != obj.owner:             # 현재 사용자 !- 객체 소유자
            return self.handle_no_permission()    # 다르면 403 exception 처리
        return super().dispatch(request,*args,**kwargs) # 상위클래스 dispatch() 실행