from locale import currency
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    email_address = models.EmailField()
    phone_number= models.CharField(max_length=15)
    gender_choices = {
        ('M','MALE')
        ('F','FEMALE')
    }
    gender = models.CharField(max_length=6)
    age = models.PositiveSmallIntegerField()
    id_number =models.CharField()
    country = models.CharField()
    account_type = models.CharField()
    registration_date = models.CharField()
    profile_picture = models.CharField()
    nationality = models.CharField()

class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer_wallet')
    amount = models.IntegerField()
    date = models.DateTimeField()
    transaction= models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='wallet_transaction')
    currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='wallet_currency')
    pin = models.IntegerField()

class Account(models.Model):
    account_number = models.IntegerField(max_length=16)
    account_type={
        ('Expenditure'),
        ('Deposit'),
        ('Withdraw'),
        ('Savings'),
        ('Fixed')
    }
    balance = models.IntegerField()
    name = models.CharField()
    Wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='account_wallet')

class Transaction(models.Model):
    transaction_charges=models.IntegerField()
    transaction_code=models.CharField()
    wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_number=models.IntegerField()
    transaction_dateTime=models.DateTimeField()
    transaction_types={
        ('Debit'),('Credit')
    }
    transaction_type=models.CharField()
    receipt=models.OneToOneField('Receipt',on_delete=models.CASCADE,related_name='transaction_receipts')
    origin_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='transaction_origin')
    destination_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='transaction_destination')

class Card(models.Model):
    card_number=models.IntegerField()
    card_name=models.CharField()
    card_types={
        ('Credit'),('Debit')
    }
    card_type=models.CharField()
    expiry_date=models.DateTimeField()
    cvv_securityCode=models.CharField()
    date=models.DateTimeField()
    wallet=models.ManyToManyField(Wallet,on_delete=models.CASCADE,related_name='wallet_card')
    account=models.ManyToManyField(Account,on_delete=models.CASCADE,related_name='card_account')
    issuers={
        ('Mastercard'),('Visacard')
    }
    issuer=models.CharField()

class ThirdParty(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='thirdparty_account')
    thirdparty_id=models.CharField()
    thirdparty_type=models.CharField()
    thirdparty_amount=models.CharField()
    thirdparty_name=models.CharField()
    currency=models.ForeignKey(currency,on_delete=models.CASCADE,related_name='thirdparty_currency')
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='thirdparty_transaction')

class Notification(models.Model):
    message=models.CharField()
    date = models.DateTimeField()
    recipient =models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='recipient_notification')
    status=models.CharField()
    statuses={
        ('Read'),('Unread')
    }
    title=models.CharField()

class Receipt(models.Model):
    receipt_type=models.CharField()
    receipt_date=models.DateTimeField()
    receipt_type=models.CharField()
    total_amount=models.IntegerField()
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='receipt_transaction')
    receiptFile=models.FileField()

class Loan(models.Model):
    loan_number=models.IntegerField()
    interest_rate=models.IntegerField()
    amount=models.IntegerField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='loan_wallet')
    loan_term=models.IntegerField()
    payment_due_date=models.DateTimeField()
    loan_balance=models.IntegerField()
    date_time=models.DateTimeField()
    guarantor=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='loan_guarantor')

class Reward(models.Model):
    name=models.CharField()
    date_of_reward=models.DateTimeField()
    recipient_wallet=models.OneToOneRel()
    transactiom=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='transaction_reward')
    transfer=models.IntegerField()
    redeem=models.IntegerField()
    shop=models.CharField()