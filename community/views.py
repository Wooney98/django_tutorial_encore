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
    return render(request, 'write.html', {'data1':hello, 'data2':hello2, 'form':form}) 


def articleList(request):
    article_list = Article.objects.all()
    return render(request, 'list.html',{'article_list':article_list})