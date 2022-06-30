from dataclasses import field
from operator import imod
from rest_framework import serializers
from accounts.models import UserBankAccount, User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model =  UserBankAccount
        fields = ('user', 'account_type', 'account_no','balance')