import os

from django.db import models
from django.conf import settings
from users.models import CustomUser


class Cart(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT))
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ('paid', 'оплачено'),
        ('new', 'новый заказ'),
        ('canceled', 'отменено'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=200)
    #phone = PhoneNumberField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return f'{self.user} - {self.total_price}'


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'Заказ {self.product.name} - {self.order.user}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=200)
    mail = models.EmailField(unique=True)

    def __str__(self):
        return self.name




