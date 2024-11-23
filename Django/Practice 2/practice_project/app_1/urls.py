
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/<int:id>', views.page, name='page'),
]
