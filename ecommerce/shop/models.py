from django.db import models

# Create your models here.

class Categories(models.Model):

    category_name = models.CharField(max_length=20)
    desc = models.TextField()
    image = models.ImageField(upload_to='cat_img',blank=True,null=True)

    def __str__(self):
        return self.category_name

class Products(models.Model):

    product_name = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.ImageField(upload_to='prod_img', blank=True, null=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    available = models.BooleanField(default=True)       # always set True
    created = models.DateTimeField(auto_now_add=True)   # automatically adds date and time when created, when creating it only adds once
    updated = models.DateTimeField(auto_now=True)      # auto_now is used in update because it adds every time it gets updated.


    category = models.ForeignKey(Categories,on_delete=models.CASCADE)   # category is a field used to connect both the tables.
                                                    # on_delete=models.CASCADE is used when referencing a table, ie here when a field from categories table is deleted the field from product table should also be deleted.
    def __str__(self):
        return self.product_name
