from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

# Create your views here.

class loginView(View):
    def get(self, request):
        return render(request, 'fourth/login.html')
    

class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('fourth:login')

    def get(self, request):
        user = request.user
        return HttpResponse(f"here is the dashboard page {user.username}")


