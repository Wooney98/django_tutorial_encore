from django.shortcuts import render, redirect
from .models import CountryData
from .forms import CountryDataForm

# Create your views here.
def dashboard(request):
    # 나라별 인구 데이터 DB에서 가져오기

# if request.method == POST
#   if valid
#       폼에 입력한 데이터 저장
# else 
#   비어있는(생성자) 폼 객체= return => GET
# 랜더링 리턴
    if request.method =='POST':
        form = CountryDataForm(request.POST)
        
        if form.is_valid():
            '''
            [중복체크구현]
            폼에 입력값을 개별로 변수대입
            나라(country) DB값이 있는지 확인
            입력한 나라 이름이 있으면, 업데이트
            없으면, 저장
            '''
            input_country=form.data.get('country',None)
            input_num=form.data.get('population',None)
            print(input_country,input_num)
            CountryData.objects.update_or_create(
                #filter
                country = input_country, # 변수에 새로 업데이트
                #new alue
                defaults={
                    'country':input_country,
                    'population':input_num
                }

            )
            #form.save()

            #return redirect('/dashboard')
            # redirect하면 else가 실행된다.
            return redirect('.') # else = 초기화 느낌?
    else:
        form = CountryDataForm()

    # 인구DB 가져오기
    country_data = CountryData.objects.all()
    
    context = {
        'country_data':country_data,
        'form':form,
    }
    return render(request, 'dashboard/dashboard.html',context)
