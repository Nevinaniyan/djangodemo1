from django.db import models
from shop.models import Products
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)  # product is a field that is set as foreignkey  that connects both Cart table to Product table.
    user = models.ForeignKey(User,on_delete=models.CASCADE)        # user is a field that connects User table to Cart table. There needs to be different cart for different users.
    quantity = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.quantity*self.product.price     # self shows each record in the cart. It is passed as function in the template, not field.

    def __str__(self):
        return self.product.product_name

class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_items = models.IntegerField()
    phone = models.IntegerField()
    address = models.TextField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered_status = models.CharField(max_length=30,default="pending")
    delivery_status = models.CharField(max_length=30,default="pending")

    def __str__(self):
        return self.user.username

class Account(models.Model):
    account_number = models.BigIntegerField()
    account_type = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.account_number)