from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payments.models import PaymentRequest, Requisite
from payments_drf.serializers import PaymentRequestSerializer, CreateInvoiceSerializer, RequisiteSerializer, \
    PaymentIdSerializers


@api_view(['GET'])
def get_invoice_status(request, *args, **kwargs):
    try:
        payment_request = PaymentRequest.objects.get(id=kwargs.get('pk'))
        serializer = PaymentRequestSerializer(payment_request)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PaymentRequest.DoesNotExist:
        return Response({'error': 'Заявка не найдена'}, status=status.HTTP_404_NOT_FOUND)


class CreateInvoice(generics.CreateAPIView):
    queryset = Requisite.objects.all()
    serializer_class = CreateInvoiceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_data = serializer.validated_data

        requisite = Requisite.objects.create(
            type_of_payment=validated_data['type_of_payment'],
            card_type='visa',
            owner_full_name="Mark",
            phone_number="+734242424",
            limit=5022
        )

        payment_request = PaymentRequest.objects.create(
            amount=validated_data['amount'],
            requisites=requisite,
            status=PaymentRequest.PENDING
        )

        return Response({
            'requisite': RequisiteSerializer(requisite).data,
            'payment_request': PaymentIdSerializers(payment_request).data
        }, status=status.HTTP_201_CREATED)
