from django.urls import path
from .import views
from .views import SearchResult

urlpatterns = [
    path('', views.home, name='home'),          ### path to home view (home page)
    path('search_result/', SearchResult.as_view(), name='search_result'),   ## path to search results view
    path('details/<int:pk>', views.article_details, name='article_details'),    ### viewing the details of article at the home page
    
]