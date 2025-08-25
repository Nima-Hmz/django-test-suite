from django.urls import path
from .views import Index, ProductsView

app_name = 'third'

urlpatterns = [
    
    path('', Index.as_view(), name='index'),
    path('products/', ProductsView.as_view(), name='products')

]