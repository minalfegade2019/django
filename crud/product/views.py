from django.shortcuts import render,redirect
from django.http import HttpResponse
from product.models import Product

# Create your views here.
def show(request):
          products=Product.objects.all()
          data={}
          data['products']=products
          return render(request,'product/show.html',context=data)

def add(request):
          if(request.method=="POST"):
                  pname=request.POST['name']
                  pprice=request.POST['price']
                  pcategory=request.POST['category']
                  print(pname,pprice,pcategory)
                  created_product=Product.objects.create(name=pname,price=pprice,category=pcategory)
                  created_product.save()
                  return redirect('/product/show')
          return render(request,'product/add.html')

def update(request,product_id):
          products=Product.objects.filter(id=product_id)
          # print(products)
          # print(products[0])
          # print(products[0].name)
          product=products[0]
          data={}
          data['product']=product
          if(request.method=="POST"):
                  pname=request.POST['name']
                  pprice=request.POST['price']
                  pcategory=request.POST['category']
                  products.update(name=pname,price=pprice,category=pcategory)
                  return redirect('/product/show')
          return render(request,'product/update.html',context=data)

def delete(request,product_id):
          product=Product.objects.get(id=product_id)
          product.delete()
          return redirect('/product/show')
