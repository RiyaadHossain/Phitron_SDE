from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='profile_page'),
    path('update_info/', views.update_info, name='update_info_page'),
    path('order_history/', views.order_history, name='order_history_page'),
]
