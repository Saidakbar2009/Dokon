from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def asosiy(request):
    return render(request, 'page-index-2.html')

def asosiy2(request):
    return render(request, 'page-index.html')

def BolimlarView(request):
    return render(request, 'page-category.html')

def MahsulotlarView(request):
    return render(request, 'page-listing-grid.html')

def MahsulotView(request):
    return render(request, 'page-detail-product.html')

