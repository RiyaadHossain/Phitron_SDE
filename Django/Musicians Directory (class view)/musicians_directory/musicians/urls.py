
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Add_Musician.as_view(), name='add_musician_page'),
    path('edit/<int:id>', views.Edit_Musician.as_view(), name='edit_musician_page')
]
