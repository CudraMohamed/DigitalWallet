# from dataclasses import fields
from django import forms    #from dgango.forms import ModelForm
from .models import Account, Customer,Currency, Notification, Receipt, Reward, ThirdParty,Transaction,Loan,Card, Wallet


class CustomerRegistrationForm(forms.ModelForm):    #(ModelForm)-importing specific class
    class Meta:
        model=Customer
        fields="__all__"
        # widgets={
        #     "gender":forms.Select(attrs={'class':"form-control"}),
        #     "profile_picture":forms.ClearableFileInput(attrs={'class':"form-control"}),
        # }

class CurrencyRegistrationForm(forms.ModelForm):    
    class Meta:
        model=Currency
        fields="__all__"

class AccountRegistrationForm(forms.ModelForm):   
    class Meta:
        model=Account
        fields="__all__"

class TransactionRegistrationForm(forms.ModelForm):    
    class Meta:
        model=Transaction
        fields="__all__"

class CardRegistrationForm(forms.ModelForm):    
    class Meta:
        model=Card
        fields="__all__"

class LoanRegistrationForm(forms.ModelForm):   
    class Meta:
        model=Loan
        fields="__all__"

class NotificationRegistrationForm(forms.ModelForm):   
    class Meta:
        model=Notification
        fields="__all__"

class ReceiptRegistrationForm(forms.ModelForm):   
    class Meta:
        model=Receipt
        fields="__all__"

class ThirdpartyRegistrationForm(forms.ModelForm):   
    class Meta:
        model=ThirdParty
        fields="__all__"

class WalletRegistrationForm(forms.ModelForm):   
    class Meta:
        model=Wallet
        fields="__all__"

class RewardRegistrationForm(forms.ModelForm):   
    class Meta:
        model=Reward
        fields="__all__"