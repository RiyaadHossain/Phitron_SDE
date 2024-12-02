from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Borrowing

def borrowing_list(req):
    borrowings = Borrowing.objects.filter(user=req.user)
    return render(req, 'borrowing_list.html', {'borrowings':borrowings})

def return_book(req, borrowid):
    borrowing = Borrowing.objects.get(pk=borrowid)
    borrowing.return_date = timezone.now().date()
    borrowing.save()

    profile = req.user.profile
    profile.balance += borrowing.book.borrowing_price
    profile.save()

    messages.success(req, f"You have complete reading book: {borrowing.book.title}")
    return redirect('borrowinglist_page')