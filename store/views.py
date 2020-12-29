from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "store/home.html")

def products(request):
    return render(request, 'store/products.html')

def customer(request):
    return render(request, 'store/customer.html')