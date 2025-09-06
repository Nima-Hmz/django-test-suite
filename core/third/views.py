from django.shortcuts import render, redirect
from django.views import View
from second.models import Products
from django.http import HttpResponse
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
    

class FormProductView(View):
    def get(self, request):
        product_form = ProductForm()
        context = {
            'product_form':product_form
        }
        return render(request, 'third/product_form_template.html', context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            product_form_data = product_form.cleaned_data

            try:
                new_product = Products(name=product_form_data['name'], price=product_form_data['price'],
                        stock_count=product_form_data['stock_count'])
                new_product.full_clean()
                new_product.save()
                return redirect('third:form_product_url')
            except Exception:
                return HttpResponse('failed to save the product')
    
        context = {'product_form':product_form}
        return render(request, 'third/product_form_template.html', context)
            
            
    


        

        