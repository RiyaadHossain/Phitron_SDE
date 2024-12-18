from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarListingView.as_view(), name='car_listing'),
    path('<int:id>/', views.car_details, name='car_details'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car')
]
