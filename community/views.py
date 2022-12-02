from django.shortcuts import render
from .forms import Form
from .models import Article

# Create your views here.
# # FBV형
# def write(request):
#     # urls에서 요청한 path write를 랜더링하라
#     # 비즈니스 로직 구현 => render(request , html 템플릿 파일, {'키':'값'} )
#     # hello = "Hello Django!!"
#     # hello2 = "HeLL 당고"


#     # if
#     # requset의 메소드가 POST이면,
#     # 사용자가 입력한 form 데이터를 변수에 저장하고,
#     # ORM으로 DB에 저장!
#     # else
#     if request.method == "POST":
#         form = Form(request.POST)
#         if form.is_valid():
#             form.save() # 필드값 저장
#     else:
#         form = Form()    
#     return render(request, 'community/write.html', {'form':form}) 


# def articleList(request):
#     article_list = Article.objects.all()
#     return render(request, 'community/list.html',{'article_list':article_list})


# def viewDetail(request, num=1):
#     #클릭한 레코드의 DB 읽어오기
#     article_detail = Article.objects.get(id=num)
#     return render(request, 'community/view_detail.html', {'article_detail':article_detail})


def index(request):
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, "index.html", {'latest_article_list':latest_article_list})



# CBV형
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from community.models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tutorial.views import OwnerOnlyMixin


class ArticleListView(ListView):
    model = Article
    template_name = 'community/list.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'community/view_detail.html'

class WriteFormView(CreateView):
    model = Article
    fields = ['name','title','contents','url','email']
    template_name = "community/write.html"
    success_url = reverse_lazy('community:list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        #폼에 연결된 모델 객체의 owner필드에 현재 로그인 된 user 객체 할당
        return super().form_valid(form)

# 변경(login user 자료만 list_up)
class ArticleChangeView(LoginRequiredMixin, ListView):
    template_name = 'community/change_list.html'
    def get_queryset(self):
        return Article.objects.filter(owner=self.request.user)
    # get_queryset()
    # 화면에 출력할 레코드 리스트 반환 
    # Article 테이블의 레코드 중에 owner 필드의 소유 레코드만 필터링 해서 리스트 반환



#로그인 user 메모 수정(Update)
class ArticleUpdateView(OwnerOnlyMixin,UpdateView):
    model = Article
    template_name = 'community/article_update.html'
    fields = ['name','title','contents','url','email']
    success_url = reverse_lazy('community:change_list')

#로그인 user 메모 삭제(Delete)
class ArticleDeleteView(OwnerOnlyMixin,DeleteView):
    model = Article
    template_name = 'community/article_delete.html'
    success_url = reverse_lazy('community:change_list')