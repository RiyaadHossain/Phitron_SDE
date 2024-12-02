from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in, name='login_page'),
    path('logout/', views.log_out, name='logout_page'),
    path('register/', views.register, name='register_page'),
    path('deposit/', views.deposit, name='deposit_page'),
]
