from django.contrib import admin
from .models import Customer
from .models import Wallet
from .models import Currency
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdParty
from .models import Notification
from .models import Receipt
from .models import Loan
from .models import Reward

# Register your models here.
# add model amin
#Access Admin dashboard

#Add a model to the admin panel
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email_address')
    search_details=('first_name','last_name')

class CurrencyAdmin(admin.ModelAdmin):
    list_display=('amount','origin_country')
    search_details=('amount','origin_country') 

class WalletAdmin(admin.ModelAdmin):
    list_display=('customer','balance','amount','currency','date','pin')
    search_details=('customer','balance','amount','currency','date','pin')

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_number','account_type','balance','name','wallet')
    search_details=('account_number','account_type','balance','name','wallet')

class TransactionAdmin(admin.ModelAdmin):
    list_display=('transaction_charges','transaction_amount','transaction_number','transaction_dateTime')
    search_details=('transaction_charges','transaction_amount','transaction_number','transaction_dateTime')

class CardAdmin(admin.ModelAdmin):
    list_display=('card_number','card_name','account','date_issued')
    search_details=('card_number','card_name','account','date_issued')

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=('account','thirdparty_id','thirdparty_amount','phone_number')
    search_details=('account','thirdparty_id','thirdparty_amount','phone_number')

class NotificationAdmin(admin.ModelAdmin):
    list_display=('message','date','recipient','title')
    search_details=('message','date','recipient','title')

class ReceiptAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_date','total_amount','receiptFile')
    search_details=('receipt_type','receipt_date','total_amount','receiptFile')

class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_number','loan_type','interest_rate','date','wallet')
    search_details=('loan_number','loan_type','interest_rate','date','wallet')

class RewardAdmin(admin.ModelAdmin):
    list_display=('name','date_of_reward','recipient_wallet','transaction','transfer')
    search_details=('name','date_of_reward','recipient_wallet','transaction','transfer')

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Currency,CurrencyAdmin)
admin.site.register(Wallet,WalletAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(ThirdParty,ThirdPartyAdmin)
admin.site.register(Notification,NotificationAdmin)
admin.site.register(Receipt,ReceiptAdmin)
admin.site.register(Loan,LoanAdmin)
admin.site.register(Reward,RewardAdmin)