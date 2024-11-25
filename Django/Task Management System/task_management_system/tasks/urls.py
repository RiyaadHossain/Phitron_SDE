from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_task, name='show_task_page'),
    path('add/', views.add_task, name='add_task_page'),
    path('edit/<int:id>', views.edit_task, name='edit_task_page'),
    path('delete/<int:id>', views.delete_task, name='delete_task_page'),
]
