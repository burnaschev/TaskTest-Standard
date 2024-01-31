from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Requisite(models.Model):
    CASH = 'cash'
    TRANSFER = 'transfer'

    payment_method_choices = (
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    )

    VISA = 'visa'
    MASTERCARD = 'mastercard'
    MIR = 'mir'

    card_types = (
        (VISA, 'Visa'),
        (MASTERCARD, 'MasterCard'),
        (MIR, 'Мир'),
    )

    type_of_payment = models.CharField(max_length=50, choices=payment_method_choices, verbose_name='метод оплаты')
    card_type = models.CharField(max_length=50, choices=card_types, **NULLABLE, verbose_name='тип карты')
    owner_full_name = models.CharField(max_length=255, verbose_name='ФИО')
    phone_number = models.CharField(max_length=20, verbose_name='телефон')
    limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='лимит')

    def __str__(self):
        return f"{self.owner_full_name} - {self.get_type_of_payment_display()}"

    class Meta:
        verbose_name = 'Реквизит'
        verbose_name_plural = 'Реквизиты'


class PaymentRequest(models.Model):
    PENDING = 'pending'
    PAID = 'paid'
    CANCELED = 'canceled'

    status_payment = (
        (PENDING, 'Ожидает оплаты'),
        (PAID, 'Оплачена'),
        (CANCELED, 'Отменена'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма')
    requisites = models.ForeignKey(Requisite, on_delete=models.CASCADE, verbose_name='реквизит')
    status = models.CharField(max_length=50, choices=status_payment, verbose_name='статус')

    def __str__(self):
        return f"ID: {self.id} - {self.get_status_display()} - {self.amount}"

    class Meta:
        verbose_name = 'Запрос на оплату'
        verbose_name_plural = 'Запросы на оплату'
