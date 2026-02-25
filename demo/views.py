from django.shortcuts import render,redirect
from .models import Items

# Create your views here.
def add_product(request):
    if request.method =="POST":
        product = request.POST["product"]
        price = request.POST["price"]

        Items.objects.create(product=product,price=price)

        return render(request, "greetings.html")
    
    return render(request, "product_form.html")


def product_list(request):
    items=Items.objects.all()

    return render(request, "products.html",{"items":items})

def update_product(request,id):
    product=Items.objects.get(id=id)
    if request.method=="POST":
        product.name=request.POST["product"]
        product.price=request.POST["price"]
        product.save()

        return redirect('product_list')
    
    return render(request, "update.html",{"product":product})