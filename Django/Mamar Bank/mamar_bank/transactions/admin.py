from django.contrib import admin
from django.contrib import messages
from .models import Transaction
from django.core.mail import send_mail
from django.conf import settings

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount', 'balance_after_transaction', 'transaction_type', 'loan_approve']
    readonly_fields = ['receiver']
    
    def save_model(self, request, obj, form, change):
        # if change and obj.loan_approve:
        #     messages.error(request, "You cannot edit this transaction as the loan is already approved.")
        #     return 
        
        obj.account.balance += obj.amount
        obj.balance_after_transaction = obj.account.balance
        obj.account.save()

        subject = "Loan Approved"
        message = "Your loan request is approved"
        recipient_list = [obj.account.user.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

        super().save_model(request, obj, form, change)

