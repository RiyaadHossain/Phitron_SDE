from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from .models import Category, Book
from borrowing.models import Borrowing
from .forms import BookReviewForm
from accounts.views import send_email_to_user


def book_list(req):
    categories = Category.objects.all()
    category_id = req.GET.get('category_id')
    books = Book.objects.all()
    if category_id:
        category = Category.objects.get(pk=category_id)
        books = Book.objects.filter(category=category)
    return render(req, 'book_list.html', {'categories': categories, 'books': books})
    
def book_details(req, bookid):
    book = Book.objects.get(pk=bookid)
    reviewForm = BookReviewForm()

    if req.method == 'POST':
        reviewForm = BookReviewForm(req.POST, user=req.user, book=book)
        if reviewForm.is_valid():
            review = reviewForm.save(commit=False)
            review.user = req.user 
            review.book = book  
            review.save()
            return redirect('bookdetails_page', bookid=book.id)

    return render(req, 'book_details.html', {'book': book, 'reviewForm': reviewForm})

def borrow_book(req, bookid):
    book = Book.objects.get(pk=bookid)
    if book.borrowing_price > req.user.profile.balance:
        messages.error(req, "Insufficiant Balance!")        
        return redirect(req.META.get('HTTP_REFERER', reverse('homepage')))

    profile = req.user.profile
    profile.balance -= book.borrowing_price
    profile.save()
    Borrowing.objects.create(book=book, user=req.user, balance_after_borrowing=profile.balance)
    messages.success(req, f"Successfully, borrow book:{book.title}!")        


    subject = "Book Borrow"
    message = f"Book: {book.title} borrowed successfully"
    recipient_list = [req.user.email]

    send_email_to_user(subject, message, recipient_list)

    return redirect('borrowinglist_page')

