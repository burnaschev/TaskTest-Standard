from django.urls import path

from .apps import PaymentsDrfConfig
from .views import CreateInvoice, get_invoice_status

app_name = PaymentsDrfConfig.name

urlpatterns = [
    path('payments/create/', CreateInvoice.as_view(), name='payments-create_invoice'),
    path('payments/get_status/<int:pk>/', get_invoice_status, name='payments-get_status')
]
