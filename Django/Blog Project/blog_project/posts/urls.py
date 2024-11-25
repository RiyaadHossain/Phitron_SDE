from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_post, name='add_post_page'),
    path('edit/<int:id>', views.edit_post, name='edit_post_page'),
    path('delete/<int:id>', views.delete_post, name='delete_post_page'),
]
