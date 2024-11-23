

from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('meal/', include('meal.urls')),
    path('admin/', admin.site.urls),
]
