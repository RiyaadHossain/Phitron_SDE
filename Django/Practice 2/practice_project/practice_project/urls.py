
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('app/', include('app_1.urls'))
]
