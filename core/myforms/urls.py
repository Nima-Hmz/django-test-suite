from .views import FirstView
from django.urls import path


app_name = 'myforms'

urlpatterns = [
    
    path('first/', FirstView.as_view(), name='first')

]
