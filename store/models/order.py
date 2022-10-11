import datetime
from django.db import models
from .item import Product
from .customer import Customer
# Create your models here.

class Order(models.Model):
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200,default='',blank=True)
    phone=models.CharField(max_length=10,default='+91',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    delivered=models.BooleanField(default=False)

    def placeorder(self):
        self.save()

    @staticmethod
    def get_orders_by_customerid(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')