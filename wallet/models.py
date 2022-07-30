from locale import currency
from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=50,null=True)
    email_address = models.EmailField(max_length=25,null=True)
    phone_number= models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=6,null=True)
    age = models.PositiveSmallIntegerField(null=True)
    id_number =models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=20,null=True)
    account_type = models.CharField(max_length=20,null=True)
    registration_date = models.CharField(max_length=20,null=True)
    profile_picture = models.CharField(max_length=20,null=True)
    nationality = models.CharField(max_length=20,null=True)

class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='wallet_customer')
    amount = models.IntegerField()
    date = models.DateTimeField()
    transaction= models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='wallet_transaction')
    currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='wallet_currency')
    pin = models.IntegerField()

class Currency(models.Model):
    amount=models.IntegerField()
    origin_country=models.CharField(max_length=25,null=True)

class Account(models.Model):
    account_number = models.IntegerField(default=0)
    account_type=models.CharField(max_length=20,null=True)
    balance = models.IntegerField()
    name = models.CharField(max_length=20,null=True)
    Wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='account_wallet')

class Transaction(models.Model):
    transaction_charges=models.IntegerField()
    transaction_code=models.CharField(max_length=200,null=True)
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_number=models.IntegerField()
    transaction_dateTime=models.DateTimeField()
    transaction_type=models.CharField(max_length=10,null=True)
    receipt=models.OneToOneField('Receipt',on_delete=models.CASCADE,related_name='transaction_receipts')
    origin_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='transaction_origin')
    destination_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='transaction_destination')

class Card(models.Model):
    card_number=models.IntegerField()
    card_name=models.CharField(max_length=20,null=True)
    card_type=models.CharField(max_length=20,null=True)
    expiry_date=models.DateTimeField()
    cvv_securityCode=models.CharField(max_length=16,null=True)
    date=models.DateTimeField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='card_wallet')
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='card_account')
    issuer=models.CharField(max_length=20,null=True)

class ThirdParty(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='thirdparty_account')
    thirdparty_id=models.CharField(max_length=20,null=True)
    phone_number=models.IntegerField()
    # thirdparty_amount=models.IntegerField()
    thirdparty_name=models.CharField(max_length=20,null=True)
    currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='thirdparty_currency')
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='thirdparty_transaction')

class Notification(models.Model):
    message=models.CharField(max_length=20,null=True)
    date = models.DateTimeField()
    recipient =models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='notification_recipient')
    status=models.CharField(max_length=20,null=True)
    title=models.CharField(max_length=20,null=True)

class Receipt(models.Model):
    receipt_type=models.CharField(max_length=20,null=True)
    receipt_date=models.DateTimeField()
    receipt_type=models.CharField(max_length=20,null=True)
    total_amount=models.IntegerField()
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='receipt_transaction')
    receiptFile=models.FileField(upload_to='wallet/')

class Loan(models.Model):
    loan_number=models.IntegerField()
    loan_type=models.CharField(max_length=25)
    interest_rate=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    amount=models.IntegerField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='loan_wallet')
    loan_term=models.IntegerField()
    payment_due_date=models.DateTimeField()
    loan_balance=models.IntegerField()
    due_date=models.DateTimeField(default=timezone.now)
    guarantor=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='loan_guarantor')

class Reward(models.Model):
    name=models.CharField(max_length=20,null=True)
    date_of_reward=models.DateTimeField()
    recipient_wallet=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='reward_receipient')
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='reward_transaction')
    transfer=models.IntegerField()
    redeem=models.IntegerField()
    shop=models.CharField(max_length=20,null=True)