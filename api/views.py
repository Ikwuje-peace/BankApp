from rest_framework import generics
from accounts.models import UserBankAccount
from .serializers import  AccountSerializer

# Create your views here.

class AccountAPIView(generics.ListAPIView):
    queryset = UserBankAccount.objects.all()
    serializer_class = AccountSerializer

class AccountDetailAPIView(generics.RetrieveAPIView):
    queryset =  UserBankAccount.objects.all()
    serializer_class = AccountSerializer
