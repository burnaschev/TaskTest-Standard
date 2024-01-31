from rest_framework import serializers

from payments.models import Requisite, PaymentRequest


class RequisiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisite
        fields = '__all__'


class PaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = ('status',)


class CreateInvoiceSerializer(serializers.Serializer):
    type_of_payment = serializers.ChoiceField(choices=Requisite.payment_method_choices)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)


class PaymentIdSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = ('id',)
