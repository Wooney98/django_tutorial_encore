from django.urls import path, include
from community import views #write,articleList, viewDetail, index

app_name="community"
urlpatterns = [
    #/write/
    #path('write/', write, name='write'), # path, view의 함수
    path('write/', views.WriteFormView.as_view(), name='write'),
   
    #/list/
    #path('list/', articleList, name="list"),
    path('list/', views.ArticleListView.as_view(), name="list"),
   
    #/view_detail/
    #path('view_detail/<int:num>/', viewDetail, name='view_detail'),
    path('view_detail/<slug:pk>/', views.ArticleDetailView.as_view(), name='view_detail'),
    
    # #/change/
    # path('change/', views.ArticleChangeView.as_view(), name='change_list'),

   
    # # /view_detail/1/update
    # path('<int:pk>/update/', views.ArticleUpdateView.as_view(), name='update'),
   
    # # /view_detail/1/delete
    # path('<int:pk>/delete', views.ArticleDeleteView.as_view(), name='delete'),
]