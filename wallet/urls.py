from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.register_customer,name="registration"),
    path("currency/",views.register_currency,name="currency"),
    path("account/",views.register_account,name="account"),
    path("transaction/",views.register_transaction,name="transaction"),
    path("wallet/",views.register_wallet,name="wallet"),
    path("card/",views.register_card,name="card"),
    path("thirdparty/",views.register_thirdparty,name="thirdparty"),
    path("notification/",views.register_notification,name="notification"),
    path("receipt/",views.register_receipt,name="receipt"),
    path("loan/",views.register_loan,name="loan"),
    path("reward/",views.register_reward,name="reward"),

    path("customers/",views.list_customers,name="customers_list"),
    path("currencys/",views.list_currencys,name="currencys_list"),
    path("accounts/",views.list_accounts,name="accounts_list"),
    path("transactions/",views.list_transactions,name="transactions_list"),
    path("wallets/",views.list_wallets,name="wallets_list"),
    path("cards/",views.list_cards,name="cards_list"),
    path("thirfparties/",views.list_thirfparties,name="thirfparties_list"),
    path("notifications/",views.list_notifications,name="notifications_list"),
    path("receipts/",views.list_receipts,name="receipts_list"),
    path("loans/",views.list_loans,name="loans_list"),
    path("rewards/",views.list_rewards,name="rewards_list"),
    ]