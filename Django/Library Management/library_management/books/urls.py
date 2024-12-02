from django.urls import path
from .views import book_list, book_details,borrow_book

urlpatterns = [
    path('', book_list, name='booklist_page'),
    path('<int:bookid>/', book_details, name='bookdetails_page'),
    path('borrow/<int:bookid>/', borrow_book, name='borrow_book'),
]
