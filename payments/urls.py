from django.urls import path

from .apps import PaymentsConfig
from .views import PaymentRequestListView, index

app_name = PaymentsConfig.name

urlpatterns = [
    path('payment/', PaymentRequestListView.as_view(), name='requisite-list'),
    path('home/', index, name='home')
]
