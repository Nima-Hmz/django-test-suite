from django.urls import path
from .views import loginView, DashboardView, PostView

app_name = 'fourth'

urlpatterns = [

    path('login/', loginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('post/', PostView.as_view(), name='post')

]