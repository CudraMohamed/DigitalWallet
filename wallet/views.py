from django.shortcuts import render, redirect
from . import forms
from . import models
# from .forms import AccountRegistrationForm, CustomerRegistrationForm, CurrencyRegistrationForm, TransactionRegistrationForm, CardRegistrationForm,LoanRegistrationForm,NotificationRegistrationForm,ReceiptRegistrationForm,RewardRegistrationForm,ThirdpartyRegistrationForm,WalletRegistrationForm

# Create your views here.
def register_customer(request):
    if request.method=='POST':
        form=forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})    #the request being made #where the request is made #dict(data to go with the template)
def list_customers(request):
    customers=models.Customer.objects.all()
    return render(request,"wallet/customers_list.html",{"customers":customers})

def customer_profile(request, id):  #connects to the path then to the url then the profile in the template
    customerz=models.Customer.objects.get(id=id)
    return render(request, "wallet/customer_profile.html",{"customerz":customerz})

def edit_customer(request,id):
    customer=models.Customer.objects.get(id=id)
    if request.method=="POST":
        form=forms.CustomerRegistrationForm(request.POST,instance=customer)

        if form.is_valid():
            return redirect("customer_profile",id=customer.id)
    else:
            form=forms.CustomerRegistrationForm(instance=customer)
            return render(request,"wallet/edit_customer.html",{"form":form})



def register_currency(request):
    if request.method=='POST':
        form=forms.CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            form=forms.CurrencyRegistrationForm()
    return render(request,"wallet/register_currency.html",{"form":form}) 
def list_currencys(request):
    currencys=models.Currency.objects.all()
    return render(request,"wallet/currencys_list.html",{"currencys":currencys})



def register_account(request):
    if request.method=='POST':
        form=forms.AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.AccountRegistrationForm()
    return render(request,"wallet/register_account.html",{"form":form}) 
def list_accounts(request):
    accounts=models.Account.objects.all()
    return render(request,"wallet/accounts_list.html",{"accounts":accounts})



def register_transaction(request):
    if request.method=='POST':
        form=forms.TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",{"form":form}) 
def list_transactions(request):
    transactions=models.Currency.objects.all()
    return render(request,"wallet/transactions_list.html",{"transactions":transactions})



def register_card(request):
    if request.method=='POST':
        form=forms.CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.CardRegistrationForm()
    return render(request,"wallet/register_card.html",{"form":form}) 
def list_cards(request):
    cards=models.Card.objects.all()
    return render(request,"wallet/cards_list.html",{"cards":cards})



def register_loan(request):
    if request.method=='POST':
        form=forms.LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"form":form}) 
def list_loans(request):
    loans=models.Loan.objects.all()
    return render(request,"wallet/loans_list.html",{"loans":loans})



def register_notification(request):
    if request.method=='POST':
        form=forms.NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{"form":form}) 
def list_notifications(request):
    notifications=models.Notification.objects.all()
    return render(request,"wallet/notifications_list.html",{"notifications":notifications})



def register_receipt(request):
    if request.method=='POST':
        form=forms.ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",{"form":form}) 
def list_receipts(request):
    receipts=models.Receipt.objects.all()
    return render(request,"wallet/receipts_list.html",{"receipts":receipts})



def register_reward(request):
    if request.method=='POST':
        form=forms.RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"form":form}) 
def list_rewards(request):
    rewards=models.Reward.objects.all()
    return render(request,"wallet/rewards_list.html",{"rewards":rewards})



def register_thirdparty(request):
    if request.method=='POST':
        form=forms.ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.ThirdpartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",{"form":form}) 
def list_thirdparties(request):
    thirdparties=models.ThirdParty.objects.all()
    return render(request,"wallet/thirdparties_list.html",{"thirdparties":thirdparties})



def register_wallet(request):
    if request.method=='POST':
        form=forms.WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=forms.WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form}) 
def list_wallets(request):
    wallets=models.Wallet.objects.all()
    return render(request,"wallet/wallets_list.html",{"wallets":wallets})