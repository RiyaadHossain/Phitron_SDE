
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_album, name='add_album_page'),
    path('edit/<int:id>', views.edit_album, name='edit_album_page'),
    path('delete/<int:id>', views.delete_album, name='delete_album_page')
]
