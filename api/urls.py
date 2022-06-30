from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from django.urls import path
from .views import AccountAPIView, AccountDetailAPIView, AccountStatementAPIView, DepositAPIView


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('', AccountAPIView.as_view()),
    path('<int:pk>/', AccountDetailAPIView.as_view()),
    path('account_statement/<int:pk>/', AccountStatementAPIView.as_view()),
    path('deposit/', DepositAPIView.as_view()),
    url(r'^$', schema_view)
]