from django.db import models
from accounts.models import User
from books.models import Book

class Borrowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    balance_after_borrowing = models.DecimalField(max_digits=10, decimal_places=2)
    borrowing_date = models.DateField(auto_now_add=True) 
    return_date = models.DateField(null=True, blank=True) 
