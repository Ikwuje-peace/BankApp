from django.urls import path
from .views import AccountAPIView, AccountDetailAPIView

urlpatterns = [
    path('', AccountAPIView.as_view()),
    path('account_no/<int:pk>/', AccountDetailAPIView.as_view()),
]