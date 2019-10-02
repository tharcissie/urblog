from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('view/<int:pk>', views.article_detail, name='article_detail'),
    path('new/', views.article_create, name='article_new'),
    path('edit/<int:pk>', views.article_update, name='article_edit'),
    path('delete/<int:pk>', views.article_delete, name='article_delete'),
    path('articles/colleges/<int:pk>', views.ArticleCollege.as_view(), name='article_by_college'),
    path('articles/user/<int:pk>', views.ArticleList.as_view(), name='article_by_user'),
    path('like/', views.article_like, name="article_like"),
    
 ]
 
