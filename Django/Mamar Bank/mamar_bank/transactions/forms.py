
from accounts.models import UserBankAccount
from django import forms
from django.db.models import Sum
from .models import Transaction
from core.models import Bank
from .constants import MAX_TRANSACTION_BALANCE

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class TransferForm(TransactionForm):
    receiver = forms.CharField(
        label="Receiver Account Number",
        required=True,
        max_length=20,
    )

    def clean_receiver(self):
        account_no = self.cleaned_data.get('receiver')

        try:
            receiver = UserBankAccount.objects.get(account_no=account_no)
        except UserBankAccount.DoesNotExist:
            raise forms.ValidationError(f"User Bank account with {account_no} doesn't exist")
        
        if self.account == receiver:
            raise forms.ValidationError(f"You cannot transfer to your account")

        return receiver

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        balance = self.account.balance

        if amount > MAX_TRANSACTION_BALANCE:
            raise forms.ValidationError(f"You cannot make any transaction above {MAX_TRANSACTION_BALANCE}.")

        if amount > balance:
            raise forms.ValidationError(f"Insufficient Balnace! You have {balance} in your account.")
        return amount
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.receiver = self.cleaned_data['receiver']
        if commit:
            instance.save()
        return instance

class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount


class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 2000000
        balance = account.balance # 1000
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )
        
        bank_reserve = Bank.objects.first().reserve_balance
        if amount > bank_reserve:
            raise forms.ValidationError("The bank is bankrupt. Unable to process the withdrawal.")

        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount

class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
                
        bank_reserve = Bank.objects.first().reserve_balance
        if amount > bank_reserve:
            raise forms.ValidationError("The bank is bankrupt. Unable to process the withdrawal.")


        return amount