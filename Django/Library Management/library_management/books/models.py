from django.db import models
from accounts.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    def __str__(self):
        return self.category_name
    

class Book(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="images/")
    borrowing_price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} {self.description} {self.borrowing_price}"
    

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField(max_length=500)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.review_text}"
