from django.shortcuts import render
from .models import CountryData

# Create your views here.
def dashboard(request):
    # 나라별 인구 데이터 DB에서 가져오기
    country_data = CountryData.objects.all()
    print(country_data)
    return render(request, 'dashboard/dashboard.html',{'country_data':country_data})