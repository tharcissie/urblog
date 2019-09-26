from django.urls import path
from .import views
from .views import SearchResult

urlpatterns = [
    path('', views.home, name='home'),
    path('search_result/', SearchResult.as_view(), name='search_result'),
    path('details/<int:pk>', views.article_details, name='article_details'),
    
]