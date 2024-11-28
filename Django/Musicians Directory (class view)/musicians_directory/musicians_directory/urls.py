
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('admin/', admin.site.urls),
    path('musicians/', include('musicians.urls')),
    path('albums/', include('album.urls')),
]
