from django.urls import path
from .views import AddBrand

urlpatterns = [
    path('add/', AddBrand.as_view())
]
