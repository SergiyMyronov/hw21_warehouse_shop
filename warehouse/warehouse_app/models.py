from django.db import models
from django.utils import timezone


class Book(models.Model):
    STATUS = (
        ('new', 'New book'),
        ('ordered', 'Ordered book'),
        ('deleted', 'Deleted book'),
    )

    ISBN = models.CharField(max_length=13)
    serial_num = models.CharField(max_length=10, unique=True)
    author_name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pubdate = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='new')
    order_num = models.IntegerField(blank=True, null=True)
    update_date = models.DateField(blank=True)

    def __str__(self):
        return f'{self.title}, Serial number:{self.serial_num}'

    def save(self, *args, **kwargs):
        self.update_date = timezone.now()
        super(Book, self).save(*args, **kwargs)


class Order(models.Model):
    STATUS = (
        ('cart', 'User cart'),
        ('fixed', 'Fixed by user'),
        ('completed', 'Completed by warehouse'),
        ('cancelled', 'Cancelled by warehouse'),
    )

    order_num = models.IntegerField()
    order_date = models.DateField()
    store_num = models.IntegerField()
    store_name = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=200)
    customer_mail = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUS, default='fixed')

    def __str__(self):
        return f'{self.order_date.strftime("%Y-%m-%d")} {str(self.order_num)}'


class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=13)
    author_name = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.ISBN
