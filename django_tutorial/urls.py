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
from community.views import index#,write,articleList, viewDetail, index


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
]
