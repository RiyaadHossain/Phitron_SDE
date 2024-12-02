from django.urls import path
from .views import borrowing_list, return_book

urlpatterns = [
    path('', borrowing_list, name="borrowinglist_page"),
    path('return_book/<int:borrowid>', return_book, name="return_book"),
]
