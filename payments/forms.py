from django import forms


class RequisiteListForm(forms.Form):
    SORT_CHOICES = [
        ('type_of_payment', 'Тип платежа'),
        ('card_type', 'Тип карты'),
        ('owner_full_name', 'ФИО'),
        ('phone_number', 'Номер телефона'),
        ('limit', 'Лимит'),
    ]

    sort_by = forms.ChoiceField(choices=SORT_CHOICES, required=False)
    sort_order = forms.ChoiceField(choices=[('asc', 'По возрастанию'), ('desc', 'По убыванию')], required=False)
    search_query = forms.CharField(max_length=255, required=False)
