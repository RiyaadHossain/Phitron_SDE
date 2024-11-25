
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='homepage'),
    path('admin/', admin.site.urls),
    path('authors/', include('authors.urls')),
    path('categories/', include('categories.urls')),
    path('profiles/', include('profiles.urls')),
    path('posts/', include('posts.urls')),
]
