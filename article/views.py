from django.shortcuts import render, redirect

# Create your views here.
from article.models import Product


def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'index.html')
    else:
        return redirect('login')


def products(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        product = Product.objects.all()
        content = {'product': product}

        return render(request, 'products.html', content)
    else:
        return redirect('login')


def productDetails(request, p_id):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        product = Product.objects.get(id=p_id)
        content = {'product': product}
        return render(request, 'product-details.html', content)
    else:
        return redirect('login')


def blog(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'blog.html')
    else:
        return redirect('login')


def blogDetails(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'blog-details.html')
    else:
        return redirect('login')


def contact(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'contact.html')
    else:
        return redirect('login')


def privacyPolicy(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'privacy-policy.html')
    else:
        return redirect('login')


def termsConditions(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, 'terms-conditions.html')
    else:
        return redirect('login')








