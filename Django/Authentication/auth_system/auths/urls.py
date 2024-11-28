from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='log_in'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.log_out, name='log_out'),
    path('changepass/', views.change_pass, name='change_pass'),
    path('changepass_/', views.change_pass_, name='change_pass_')
]
