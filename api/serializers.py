from rest_framework import serializers
from wallet.models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","last_name","address",
        "email_address","phone_number","gender",
        "age","id_number","country","account_type",
        "registration_date","profile_picture","nationality")
# Create serializers, views and routes for these models.
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wallet
        fields=("balance","customer","amount","date","currency","pin")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields=("account_number","account_type","balance","name","wallet")

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields=("card_number","card_name","card_type","expiry_date",
        "cvv_securityCode","date_issued","account","card_status")

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=("transaction_charges","transaction_amount",
        "transaction_number","transaction_dateTime","transaction_type",
        "receipt","destination_account")

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields=("loan_number","loan_type","interest_rate","date","amount",
        "wallet","loan_term","loan_balance","payment_due_date","guarantor")

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receipt
        fields=("receipt_type","receipt_date","receipt_type","total_amount","receiptFile")

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=("message","date","recipient","status","title")