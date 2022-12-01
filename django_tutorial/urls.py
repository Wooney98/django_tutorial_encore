"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from community.views import index#,write,articleList, viewDetail, 
from .views import UserCreateView,UserCreateDoneTV
# -> django_tutorials엔 view가 없어서 인식 못하는중
# 그러므로 views를 만들자!!

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('write/', write, name='write'), # path, view의 함수
    # path('list/', articleList, name="list"),
    # path('view_detail/<int:num>/', viewDetail, name='view_detail'),
    
    path('community/', include('community.urls')),
    # community 폴더에 urls.py를 따로 생성하고, community/urls.py안에 
    # write,list,view_detail의 path를 정하고,
    # main urls인 이곳에서 community를 include한다.
    # 즉, url의 route를 변경한것이다.
    path('', index, name='index'),

    path('dashboard/', include('dashboard.urls')),

    ### Login 인증 path ###
    # Django의 내장되어있는 urls
    path('accounts/', include("django.contrib.auth.urls")),
    # 가입처리
    # class형의 UserCreateView이기에 as_view()를 사용한다.
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    # 계정생성이 완료되었다는 메시지
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done')
]
