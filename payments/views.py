from django.shortcuts import render
from django.views.generic import ListView

from payments.models import PaymentRequest


def index(request):
    return render(request, 'payments/home.html')


class PaymentRequestListView(ListView):
    model = PaymentRequest
    template_name = 'payments/payment_list.html'
    paginate_by = 50
    ordering = ['id']
