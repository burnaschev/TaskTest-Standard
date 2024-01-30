from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from payments.models import PaymentRequest, Requisite
from payments.forms import RequisiteListForm


def index(request):
    return render(request, 'payments/home.html')


class PaymentRequestListView(ListView):
    model = PaymentRequest
    template_name = 'payments/payment_list.html'
    paginate_by = 50
    ordering = ['id']


class RequisiteListView(ListView):
    model = Requisite
    template_name = 'payments/requisite_list.html'
    paginate_by = 50
    ordering = 'id'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = RequisiteListForm(self.request.GET)
        if form.is_valid():
            sort_by = form.cleaned_data.get('sort_by')
            sort_order = form.cleaned_data.get('sort_order')
            search_query = form.cleaned_data.get('search_query')

            if search_query:
                queryset = queryset.filter(
                    Q(type_of_payment__icontains=search_query) |
                    Q(card_type__icontains=search_query) |
                    Q(owner_full_name__icontains=search_query) |
                    Q(phone_number__icontains=search_query) |
                    Q(limit__icontains=search_query)
                )

            if sort_by:
                if sort_order == 'asc':
                    queryset = queryset.order_by(sort_by)
                elif sort_order == 'desc':
                    queryset = queryset.order_by(f'-{sort_by}')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_form'] = RequisiteListForm(self.request.GET)
        return context
