
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.Add_Album.as_view(), name='add_album_page'),
    path('edit/<int:id>', views.Edit_Album.as_view(), name='edit_album_page'),
    path('delete/<int:id>', views.Delete_Album.as_view(), name='delete_album_page')
]
