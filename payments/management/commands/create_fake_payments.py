import random

from django.core.management.base import BaseCommand
from django_seed import Seed

from payments.models import Requisite, PaymentRequest


class Command(BaseCommand):

    def handle(self, *args, **options):
        seeder_requisite = Seed.seeder()
        seeder_requisite.add_entity(Requisite, 100, {
            'type_of_payment': lambda x: seeder_requisite.faker.random_element(
                elements=('Перевод на счет', 'Наличные')),
            'card_type': lambda x: seeder_requisite.faker.random_element(elements=('Visa', 'Mastercard', 'Mir')),
            'owner_full_name': lambda x: seeder_requisite.faker.name(),
            'phone_number': lambda x: seeder_requisite.faker.phone_number(),
            'limit': lambda x: seeder_requisite.faker.random_number(digits=5)
        })
        seeder_requisite.execute()

        seeder_payment = Seed.seeder()
        requisites = Requisite.objects.all()
        seeder_payment.add_entity(PaymentRequest, 5000, {
            'amount': lambda x: seeder_payment.faker.random_number(digits=4),
            'requisites': lambda x: random.choice(requisites),
            'status': lambda x: seeder_payment.faker.random_element(elements=('Ожидает оплаты', 'Оплачена', 'Отменена'))
        })
        seeder_payment.execute()
