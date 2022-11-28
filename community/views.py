from django.shortcuts import render

# Create your views here.
def write(request):
    # urls에서 요청한 path write를 랜더링하라
    # 비즈니스 로직 구현 => render(request , html 템플릿 파일, {'키':'벨류'} )
    hello = "Hello Django!!"
    hello2 = "HeLL 당고"
    return render(request, 'write.html', {'data1':hello, 'data2':hello2}) 