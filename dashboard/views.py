from django.shortcuts import render
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
    # 나라별 인구 데이터 DB에서 가져오기
    country_data = CountryData.objects.all()
    print(country_data)

# if request.method == POST
#   if valid
#       폼에 입력한 데이터 저장
# else 
#   비어있는(생성자) 폼 객체= return => GET
# 랜더링 리턴
    if request.method =='POST':
        form = CountryDataForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CountryDataForm()

    context = {
        'country_data':country_data,
        'form':form,
    }
    return render(request, 'dashboard/dashboard.html',context)
