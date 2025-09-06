from django.urls import path
from .views import Index, ProductsView, FormProductView

app_name = 'third'

urlpatterns = [
    
    path('', Index.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/form/', FormProductView.as_view(), name='form_product_url')

]