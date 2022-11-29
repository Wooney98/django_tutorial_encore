from django.shortcuts import render
from .forms import Form
from .models import Article

# Create your views here.
def write(request):
    # urls에서 요청한 path write를 랜더링하라
    # 비즈니스 로직 구현 => render(request , html 템플릿 파일, {'키':'값'} )
    hello = "Hello Django!!"
    hello2 = "HeLL 당고"
    form = Form()

    # if
    # requset의 메소드가 POST이면,
    # 사용자가 입력한 form 데이터를 변수에 저장하고,
    # ORM으로 DB에 저장!
    # else
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save() # 필드값 저장
    else:
        form = Form()    
    return render(request, 'community/write.html', {'data1':hello, 'data2':hello2, 'form':form}) 


def articleList(request):
    article_list = Article.objects.all()
    return render(request, 'community/list.html',{'article_list':article_list})


def viewDetail(request, num=1):
    #클릭한 레코드의 DB 읽어오기
    article_detail = Article.objects.get(id=num)
    return render(request, 'community/view_detail.html', {'article_detail':article_detail})


def index(request):
    latest_article_list = Article.objects.all().order_by('-cdate')[:3]
    return render(request, "index.html", {'latest_article_list':latest_article_list})