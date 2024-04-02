from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from shop.models import Products
from cart.models import Cart, Order, Account


# Create your views here.

# for display the cart

def cart_view(request):
    u = request.user
    c = Cart.objects.filter(user=u)  # filter the current user 'u' with the user in the cart table.   This picks up the cart objects and displays it.
    total = 0  # for finding the total amount at checkout.
    for i in c:  # i defines each products in c.
        total = total + i.quantity * i.product.price  # total + each quantity * its price.

    return render(request, 'cart.html', {'c': c, 'total': total})


@login_required()
def addtocart(request, p):
    p = Products.objects.get(id=p)  # getting the particular product
    u = request.user  # to get the details and records of the current user login

    try:
        c = Cart.objects.get(user=u,product=p)  # this is to check if the cart has that particular product already for the user.
        if (p.stock > 0):  # only increment till stock is available
            c.quantity += 1  # if the cart already has the product for the user, then increment quantity by '1'.
            c.save()  # save the cart details.
            p.stock -= 1  # to decrement the stock value when products are added to the cart
            p.save()  # save p

    except:  # if cart doesnt have that product for the user then create a new record for the cart.
        if (p.stock > 0):
            c = Cart.objects.create(product=p, user=u,quantity=1)  # creates a new record in the cart table with product,user,and quantity as '1' initially.
            c.save()
            p.stock -= 1
            p.save()

    return cart_view(request)


def cart_remove(request, p):
    p = Products.objects.get(id=p)  # getting the particular product
    u = request.user  # to get the details and records of the current user login

    try:
        c = Cart.objects.get(user=u,product=p)  # this is to check if the cart has that particular product already for the user.
        if (c.quantity > 1):
            c.quantity -= 1  # it decrements the quantity
            c.save()  # save the cart details.
            p.stock += 1  # it increments the available the stock.
            p.save()  # save p
        else:
            c.delete()
            p.stock += 1
            p.save()

    except:
        pass

    return cart_view(request)


def cart_empty(request, p):  # to empty the record
    p = Products.objects.get(id=p)  # getting the particular product
    u = request.user  # to get the details and records of the current user login

    try:
        c = Cart.objects.get(user=u,
                             product=p)  # this is to check if the cart has that particular product already for the user.
        c.delete()  # delete the particular products
        p.stock = p.stock + c.quantity  # stock gets added with the full quantity of the removed products
        p.save()

    except:
        pass

    return cart_view(request)


@login_required
def orderform(request):
    if request.method == "POST":
        a = request.POST['ad']
        n = request.POST['ac']
        p = request.POST['ph']

        u = request.user  # finding the user who is ordering
        c = Cart.objects.filter(user=u)  # getting the cart details of the user

        total = 0
        for i in c:
            total = total + i.quantity * i.product.price  # finding total amount from the cart

        try:
            ac_no = Account.objects.get(account_number=n)  # checking if the account number entered in the form exists in the Account table.
            if ac_no.amount >= total:  # if amount in Account is sufficient
                ac_no.amount = ac_no.amount - total  # decrement the amount from the account_number
                ac_no.save()
                for i in c:  # each record from cart
                    o = Order.objects.create(user=u, product=i.product, address=a, phone=p, no_of_items=i.quantity,ordered_status="paid")  # product and no_of_items in the order table are taken from the Cart table.
                    o.save()

                c.delete()  # the cart is emptied after the order is complete
                msg = "Order Placed Successfully"
                return render(request, 'orderdetail.html', {'message': msg})
            else:
                msg = "Insufficient Amount. Order not Placed."
                return render(request, 'orderdetail.html', {'message': msg})


        except:
            pass

    return render(request, 'orderform.html')

def your_orders(request):

    u = request.user
    o = Order.objects.filter(user=u)  # getting the cart details of the user

    return render(request,'order_page.html',{'user':u,'orders':o})
