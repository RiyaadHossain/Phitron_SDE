
from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserBankAccountUpdateView, log_out
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]