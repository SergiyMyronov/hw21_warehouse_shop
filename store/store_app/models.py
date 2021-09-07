from datetime import datetime

from django.db import models
from django.utils import timezone


class Store(models.Model):
    name = models.CharField(max_length=100)
    store_num = models.IntegerField()
    last_update_date = models.DateField(default=datetime.strptime('1901-01-01', '%Y-%m-%d'))

    def __str__(self):
        return self.name


class Book(models.Model):
    ISBN = models.CharField(max_length=13, unique=True)
    author_name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pubdate = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    STATUS = (
        ('cart', 'User cart'),
        ('fixed', 'Fixed by user'),
        ('completed', 'Completed by warehouse'),
        ('cancelled', 'Cancelled by warehouse'),
    )

    order_num = models.IntegerField(default=999999)
    order_date = models.DateField(default=timezone.now)
    store_num = models.IntegerField(default=1)
    store_name = models.CharField(default='Store1', max_length=100)
    customer_name = models.CharField(max_length=200)
    customer_mail = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS, default='cart')

    def __str__(self):
        return f'{self.order_date.strftime("%Y-%m-%d")} {str(self.order_num)}'


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    ISBN = models.CharField(max_length=13)
    author_name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.ISBN
