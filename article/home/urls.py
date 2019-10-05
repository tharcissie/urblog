from django.urls import path
from .import views
from .views import SearchResult

urlpatterns = [
    path('', views.home, name='home'),          ### path to home view (home page)
    path('search_result/', SearchResult.as_view(), name='search_result'),   ## path to search results view
    path('details/<int:pk>', views.article_details, name='article_details'),    ### viewing the details of article at the home page
    path('tag/<slug>/',views.TagListView.as_view(), name='tagged'),
    # path('articles/user/<int:pk>', views.ArticleList.as_view(), name='article_by_user'),
    path('details/<int:pk>/like/', views.ArticleLikeToggle.as_view(), name='like_toggle'), #like path
    path('details/<int:pk>/dislike/', views.ArticleDislikeToggle.as_view(), name='dislike_toggle'),#dislike path
]