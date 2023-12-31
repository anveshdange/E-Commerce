from django.shortcuts import render
from django.http import HttpResponse
from . models import item
from . models import contact_us

from math import ceil

def index(request):
    allProds = []
    catprods = item.objects.values('category', 'id')
    cats = {items['category'] for items in catprods}
    for cat in cats:
        prod = item.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allProds}
    return render(request,"shop/index.html", params)
def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact_item = contact_us(Name=name, email=email, phone=phone, desc=desc)
        contact_item.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')
def productView(request, myid):
    product = item.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodView.html", {'product': product[0]})
def checkout(request):
    return render(request, 'shop/checkout.html')
