from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # path('like/', views.like_article, name='like_article'),
    path('view/<int:pk>', views.article_detail, name='article_detail'),
    # path('view/<int:upvote_id>/upvote/', views.upvote, name='upvote'),
    path('new', views.article_create, name='article_new'),
    path('edit/<int:pk>', views.article_update, name='article_edit'),
    path('delete/<int:pk>', views.article_delete, name='article_delete'),


    path('articles/colleges/<int:pk>', views.ArticleCollege.as_view(), name='article_by_college'),
    path('articles/user/<int:pk>', views.ArticleList.as_view(), name='article_by_user'),
   
    
 ]
 
