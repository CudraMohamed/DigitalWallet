from django.db import models
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=50,null=True)
    email_address = models.EmailField(max_length=25,null=True)
    phone_number= models.CharField(max_length=15,null=True)
    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female')
    )
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    age = models.PositiveSmallIntegerField()
    id_number =models.CharField(max_length=20,null=True)
    country = models.CharField(max_length=20,null=True)
    account_type = models.CharField(max_length=20,null=True)
    registration_date = models.DateTimeField(default=timezone.now)
    profile_picture = models.ImageField(upload_to='profile_picture/')
    nationality = models.CharField(max_length=20,null=True)

class Currency(models.Model):
    amount=models.IntegerField()
    origin_country=models.CharField(max_length=25,null=True)

class Account(models.Model):
    account_number = models.IntegerField(default=0)
    account_type=models.CharField(max_length=20,null=True)
    balance = models.IntegerField()
    name = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Account_name')
    wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')

class Transaction(models.Model):
    transaction_charges=models.IntegerField()
    # wallet = models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Transaction_wallet')
    transaction_amount=models.IntegerField()
    transaction_number=models.IntegerField()
    transaction_dateTime=models.DateTimeField(default=timezone.now)
    TRANSACTION_CHOICE=(
        ('withdraw','Withdrawal'),
        ('depo','deposit')
    )
    transaction_type=models.CharField(max_length=10,choices=TRANSACTION_CHOICE,null=True)
    receipt=models.ForeignKey('Receipt',on_delete=models.CASCADE,related_name='Transaction_receipt')
    # origin_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_origin_account')
    destination_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Transaction_destination_account')

class Wallet(models.Model):
    balance = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Wallet_customer')
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    # transaction= models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='wallet_transaction')
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='Wallet_currency')
    # account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Wallet_account')
    pin = models.IntegerField()

class Card(models.Model):
    card_number=models.IntegerField()
    card_name=models.CharField(max_length=20,null=True)
    ISSUER_CHOICES=(
        ('Master','Mstercard'),
        ('Visa','Visacard')
    )
    card_type=models.CharField(max_length=20,choices=ISSUER_CHOICES,null=True)
    expiry_date=models.DateTimeField(default=timezone.now)
    cvv_securityCode=models.CharField(max_length=16,null=True)
    date_issued=models.DateTimeField(default=timezone.now)
    # wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Card_wallet')
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Card_account')
    STATUS_CHOICE=(
        ('d','debit'),
        ('c','credit')
    )
    card_status=models.CharField(max_length=1,choices=STATUS_CHOICE,null=True)

class ThirdParty(models.Model):
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='ThirdParty_account')
    thirdparty_id=models.CharField(max_length=20,null=True)
    phone_number=models.IntegerField()
    thirdparty_amount=models.IntegerField()
    thirdparty_name=models.CharField(max_length=20,null=True)
    currency=models.ForeignKey(Currency,on_delete=models.CASCADE,related_name='Thirdparty_currency')
    # transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='Thirdparty_transaction')

class Notification(models.Model):
    message=models.CharField(max_length=200,null=True)
    date = models.DateTimeField(default=timezone.now)
    recipient =models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='Notification_recipient')
    STATUS_CHOICES=(
        ('read','read'),
        ('unread','unread')
    )
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,null=True)
    title=models.CharField(max_length=20,null=True)

class Receipt(models.Model):
    receipt_type=models.CharField(max_length=20,null=True)
    receipt_date=models.DateTimeField(default=timezone.now)
    receipt_type=models.CharField(max_length=20,null=True)
    total_amount=models.IntegerField()
    # account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name='Receipt_account')
    # transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='Receipt_transaction')
    receiptFile=models.FileField(upload_to='wallet/')

class Loan(models.Model):
    loan_number=models.IntegerField()
    loan_type=models.CharField(max_length=25,null=True)
    interest_rate=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    amount=models.IntegerField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Loan_wallet')
    loan_term=models.IntegerField()
    loan_balance=models.IntegerField()
    payment_due_date=models.DateTimeField(default=timezone.now)
    guarantor=models.ForeignKey(ThirdParty,on_delete=models.CASCADE,related_name='Loan_guarantor')

class Reward(models.Model):
    name=models.CharField(max_length=20,null=True)
    date_of_reward=models.DateTimeField(default=timezone.now)
    recipient_wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='Reward_receipient_wallet')
    transaction=models.ForeignKey(Transaction,on_delete=models.CASCADE,related_name='Reward_transaction')
    transfer=models.IntegerField()
    redeem=models.IntegerField()
    shop=models.CharField(max_length=20,null=True)