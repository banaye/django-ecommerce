from django.shortcuts import render,redirect
from Store.forms import UserLoginForm, UserRegistrationForm
from Store.forms import ProductForm
from Store.models import User, Product


# Create your views here.
def index(request):
    """
    Render the index page of the E-commerce application.
    """
    return render(request, 'Store/index.html')



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # or wherever you want
    else:
        form = UserRegistrationForm()
    return render(request, 'Store/register.html', {'form': form})



def products(request):
    """
    Render the products page of the E-commerce application.
    """
    products = Product.objects.all()
    return render(request, 'Store/products.html', {'products': products})
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')  # or wherever you want
    else:
        form = ProductForm()
    
    return render(request, 'Store/products.html', {'form': form})





