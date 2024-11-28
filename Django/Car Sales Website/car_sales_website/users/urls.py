from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='signup_page'),
    path('login/', views.log_in, name='login_page'),
    path('logout/', views.log_out, name='logout_page'),
]
