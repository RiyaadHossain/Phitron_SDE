from django.urls import path
from . import views

urlpatterns = [
    path('bootstarp_form/', views.bootstarp_form, name='bootstarp_form'),
    path('built_in_form/', views.built_in_form, name='built_in_form'),
    path('form_attr_widget/', views.form_attr_widget, name='form_attr_widget'),
    path('file_upload/', views.file_upload, name='file_upload'),
    path('form_field/', views.form_field, name='form_field'),
    path('form_validation/', views.form_validation, name='form_validation'),
    path('view_data/', views.view_data, name='view_data'),
]
