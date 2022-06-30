from rest_framework import serializers
from accounts.models import UserBankAccount
from transactions.constants import TRANSACTION_TYPE_CHOICES
from transactions.models import Transaction
from transactions.forms import DepositForm


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model =  UserBankAccount
        fields = ('user','account_no','balance')

class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('account','timestamp','transaction_type','amount', 'balance_after_transaction')

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_type', 'amount')

class WithdrawSerializer(serializers.ModelSerializer):
    pass
        







