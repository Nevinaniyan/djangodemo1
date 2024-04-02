from django.contrib import admin
from cart.models import Cart,Order,Account
from django.http import HttpResponse

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Account)