from django.forms import ModelForm

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'order_num',
            'order_date',
            'store_num',
            'store_name',
            'customer_name',
            'customer_mail',
            'status',
        ]
