from django.urls import path, include
from community.views import write,articleList, viewDetail#, index

urlpatterns = [
    path('write/', write, name='write'), # path, view의 함수
    path('list/', articleList, name="list"),
    path('view_detail/<int:num>/', viewDetail, name='view_detail'),
]