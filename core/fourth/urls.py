from django.urls import path
from .views import loginView, DashboardView

app_name = 'fourth'

urlpatterns = [

    path('login/', loginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

]