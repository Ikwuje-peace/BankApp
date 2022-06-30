from dataclasses import field
from operator import imod
from unittest.util import _MAX_LENGTH
from urllib import request
from rest_framework import serializers
from accounts.models import UserBankAccount, User
from transactions.models import Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model =  UserBankAccount
        fields = ('accountName','account_no','balance')

        







