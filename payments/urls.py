from django.urls import path

from .apps import PaymentsConfig
from .views import PaymentRequestListView, index, RequisiteListView

app_name = PaymentsConfig.name

urlpatterns = [
    path('payment/', PaymentRequestListView.as_view(), name='payment-list'),
    path('requisite/', RequisiteListView.as_view(), name='requisite-list'),
    path('home/', index, name='home')
]
