from django.db import models
from product.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    customer_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    # quantity=models.PositiveIntegerField(default=1)
    # price=models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return self.order