from .views import FirstView, SecondView
from django.urls import path


app_name = 'myforms'

urlpatterns = [
    
    path('first/', FirstView.as_view(), name='first'),
    path('second', SecondView.as_view(), name='second'),

]
