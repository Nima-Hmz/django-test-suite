from django.urls import path
from .views import Index, ProductsView, SecondProductsView

app_name = 'third'

urlpatterns = [
    
    path('', Index.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('second-products/', SecondProductsView.as_view(), name='second_product'),

]