from django.shortcuts import render
from django.views import View
from second.models import Products
from .forms import ProductForm

# Create your views here.

class Index(View):
    def get(self, request):
        return render(request, 'third/index.html')
    

class ProductsView(View):
    def get(self, request):
        products = Products.objects.all()
        context = {
            "products":products
        }
        return render(request, 'third/products.html', context)
    

class SecondProductsView(View):
    def get(self, request):
        products = Products.objects.all()
        product_form = ProductForm()

        context = {
            'products':products,
            'product_form':product_form,
        }

        return render(request, 'third/second_product.html', context)
    
    def post(self, request):
        pass 
        