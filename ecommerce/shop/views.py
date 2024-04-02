from django.shortcuts import render,redirect,HttpResponse
from shop.models import Categories,Products

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def allcategories(request):
    c= Categories.objects.all()
    return render(request,'category.html',{'c':c})


# for displaying products under a particular category
@login_required()
def allproducts(request,p):
    c = Categories.objects.get(id=p)  # to retrieve a certain category using id
    p = Products.objects.filter(category=c)  # to retrieve products from a category.
    # filter is used to retrieve one or more elements according to condition
    return render(request,'product.html',{'c': c, 'p': p})

# Retrieving Category: Categories.objects.get(id=p) retrieves a single category object from
# the Categories model whose id matches the value of p.

# Retrieving Products: Products.objects.filter(category=c) retrieves all products from the Products
# model that belong to the category c. Here, c is the category object obtained in the previous step.

def home(request):
    return render(request,'home.html')

@login_required()
def details(request,p):
    p = Products.objects.get(id=p)    # here we only want one product, so we use get.
    return render(request,'details.html',{'p': p})


def register(request):
    if (request.method == "POST"):
        us = request.POST['u']       # storing the inputs from all the fields.
        pas = request.POST['p']
        conf = request.POST.get('cp')
        em = request.POST.get('e')
        fn = request.POST.get('f')
        ln = request.POST.get('l')

        if(conf==pas):        # checks if the passwords are same, if they match then only a user is created within the fields.
            new_user = User.objects.create_user(username=us,password=pas,email=em,first_name=fn,last_name=ln)  # these are inbuilt fields and these field names are predefined in the user.Model.
            new_user.save()
            return render(request,'login.html')         # redirect is used because, we want to go to book.views.home but book is another application, so we use rediredct.
        else:
            return HttpResponse("password does not match")     # if doesnt match login fails.

    return render(request,'register.html')


def login_user(request):
    if(request.method=="POST"):
        us1 = request.POST.get('u')      # the entered inputs from login page are stored in a variable.
        pas1 = request.POST.get('p')

        user = authenticate(username=us1,password=pas1)      # an instance user is created  and here the inputs are passed to th built-in function authenticate,
                                                             # it checks the input in the user that we gave in login and compares it with the username and password in the user table.
        if user:
            login(request,user)
            return redirect('shop:all_cat')                    # redirects to home page if credentials match.
        else:
            return HttpResponse("Invalid User")              # if it doesn't match invalid user is displayed.

    return render(request,'login.html')


def user_logout(request):
    logout(request)      # logout function of auth,function from django.contrib.auth module handles logging out the user,
    return home(request)     # return to the login page after logout.