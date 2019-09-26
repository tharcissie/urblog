from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from accounts import views

urlpatterns = [
    
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('articles/', include('carticle.urls')),
    
   
    
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
