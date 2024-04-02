from cart.models import Cart


def total(request):
    count = 0

    if request.user.is_authenticated:    # user should be logged in to receive current user.

        u = request.user
        try:
            c = Cart.objects.filter(user=u)    # filter the cart objects of the user
            for i in c:
                count += i.quantity            # counts the quantity of the objects.
        except:
            count = 0

    return {'count': count}         # passed in base.html

#  to show the total count of the products in the cart
