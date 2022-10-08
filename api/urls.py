from django.urls import path,include
from rest_framework import routers
from .views import *

router=routers.DefaultRouter()
router.register("customers", CustomerViewSet)
router.register("wallets", WalletViewSet)
router.register("accounts", AccountViewSet)
router.register("cards", CardViewSet)
router.register("transactions", TransactionViewSet)
router.register("loans", LoanViewSet)
router.register("receipts", ReceiptViewSet)
router.register("notifications", NotificationViewSet)

urlpatterns=[
    path("",include(router.urls)),
]