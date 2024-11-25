
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_musician, name='add_musician_page'),
    path('edit/<int:id>', views.edit_musician, name='edit_musician_page')
]
