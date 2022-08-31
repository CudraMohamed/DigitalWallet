from django.urls import path
from .views import register_account, register_currency, register_customer, register_transaction,register_card,register_wallet,register_thirdparty,register_notification,register_loan,register_receipt,register_reward

urlpatterns=[
    path("register/",register_customer,name="registration"),
    path("currency/",register_currency,name="currency"),
    path("account/",register_account,name="account"),
    path("transaction/",register_transaction,name="transaction"),
    path("wallet/",register_wallet,name="wallet"),
    path("card/",register_card,name="card"),
    path("thirdparty/",register_thirdparty,name="thirdparty"),
    path("notification/",register_notification,name="notification"),
    path("receipt/",register_receipt,name="receipt"),
    path("loan/",register_loan,name="loan"),
    path("reward/",register_reward,name="reward"),
    ]