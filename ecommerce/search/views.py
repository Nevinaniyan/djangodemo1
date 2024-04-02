from django.shortcuts import render
from shop.models import Products
from django.db.models import Q


# Create your views here.

def search(request):
    p = None  # p is set to null if there is no value in p
    query = ""  # q is set empty if incase no value is given to search
    if request.method == "POST":  # accessing the form after submitting.
        query = request.POST['q']  # getting the value entered in the form to the function
        # query = request.POST['q']: Inside the if block, this line retrieves the value of the form field named 'q'
        # from the POST data  submitted with the form. The 'q' field is commonly used for search queries.
        # The request.POST attribute is a dictionary-like object containing data submitted with the POST request.
        # print(query)
        if query:  # checking if query value matches with records
            p = Products.objects.filter(Q(product_name__icontains=query) | Q(desc__icontains=query))  # here filter is used
    return render(request, 'search_page.html', {'p': p, 'q': query})
# Q is an object used when conditions are used inside a django query. Here |('or) is used.
# if query has a value that matches the record then it returns according to condition.
# name__contains checks if the entered query matches with name.
# __contains only checks in lower case, while __icontains checks both lower and upper case.
