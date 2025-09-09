from django.urls import path
from .views import loginView, DashboardView, PostView, PostView2

app_name = 'fourth'

urlpatterns = [

    path('login/', loginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('post/', PostView.as_view(), name='post'),
    path('post2/', PostView2.as_view(), name='post2')

]