from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/home.html', {'title' : 'AimolUA' })

def about(request):
    return render(request, 'main/about.html', {'title':'Про нас'})

def product(request):
    return render(request, 'main/product.html',{'title':'Продукти'})

def contact(request):
    return render(request, 'main/contact.html',{'title':'Контакти'})

