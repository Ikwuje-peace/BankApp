from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import UserBankAccount
from transactions.models import Transaction
from .permissions import HasAccount
from .serializers import  AccountSerializer, AccountDetailSerializer, DepositSerializer, WithdrawSerializer

# Create your views here.

class AccountAPIView(generics.ListAPIView):
    queryset = UserBankAccount.objects.all()
    serializer_class = AccountSerializer

class AccountDetailAPIView(generics.RetrieveAPIView):
    queryset =  UserBankAccount.objects.all()
    serializer_class = AccountSerializer

class AccountStatementAPIView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = AccountDetailSerializer

class DepositAPIView(generics.CreateAPIView):
    permission_classes = (HasAccount,)
    queryset = Transaction
    serializer_class = DepositSerializer

class WithdrawAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (HasAccount,)
    queryset = Transaction
    serializer_class = WithdrawSerializer
